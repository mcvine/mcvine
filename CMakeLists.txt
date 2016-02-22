# To improve
# * dependency items are declared at different places
#   - This file two places 
#     - CPACK_DEBIAN_PACKAGE_DEPENDS: all deb pkgs needed during install
#     - DOCKER_PKGING_DEPS_DEB: all deb pkgs needed in building
#   - File rpm.spec.in
# * rpm and deb releases are treated differently:
#   - rpm: source rpm
#   - deb: binary deb

set(PROJECT_NAME "mcvine")
set(VERSION "1.0")
set(AUTHOR "Jiao Lin")
set(AUTHOR_EMAILE "jiao.lin@gmail.com")
set(VENDOR "DANSE")
set(SUMMARY "Monte Carlo VIrtual Neutron Experiment")
set(LICENSE "BSD")
set(RPM_APP_GROUP "Development/Tools")
set(GITHUB_URL "https://github.com/mcvine/mcvine")

# Is this still needed?
# this is released with danse.ins packages
# set(DEP_DANSE_PKGS "pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops")

# packaging with the help of docker and packagecloud
# package repository at packagecloud
set (PKGCLOUD_USERNAME "danse")
set (PKGCLOUD_REPO "ins")
# dependencies
set (DOCKER_PKGING_DEPS_DEB "python-yaml python-numpy python-psutil python-h5py python-mpi4py libgsl0-dev libboost-python-dev libboost-python1.55.0 pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops")
set (DOCKER_PKGING_DEPS_RPM "danse.ins")
set (DOCKER_PKGING_TEST_SRPM ". /opt/danse/bin/setup-danse.sh && mcvine")
set (DOCKER_PKGING_BUILDSTEP_BUILDCMD "cd .. && git clone https://github.com/mcvine/resources.git &&  /work/src/builders/build /work/src /work/build /opt/danse /work/resources")
set (DOCKER_PKGING_TEST_RPM ${DOCKER_PKGING_TEST_SRPM})
set (DOCKER_PKGING_TEST_DEB ${DOCKER_PKGING_TEST_SRPM})

#
project (${PROJECT_NAME})
cmake_minimum_required (VERSION 2.8.12)

# get cmake_utils
execute_process(
  COMMAND rm -rf cmake_utils
  )
execute_process(
  COMMAND git clone https://github.com/danse-inelastic/cmake_utils
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
set(CMAKE_MODULE_PATH ${PROJECT_BINARY_DIR}/cmake_utils)

# use utils
include(System) # system info
include(Dirs)   # directory structure
include(TestUtils)
# message("lib: $ENV{LD_LIBRARY_PATH}; python: $ENV{PYTHONPATH}")

# needs python
find_package ( PythonLibs REQUIRED )
find_package ( PythonInterp REQUIRED )
# python installation path
set(INSTALL_PY_PATH "${INSTALL_LIB_DIR}/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages")
# needs boost python
find_package ( Boost COMPONENTS python )

#
enable_testing()

# subdirs
set(BUILDING_MCVINE "yes")
# create empty cmake file for mcstas2/components
execute_process(COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_SOURCE_DIR}/packages/legacycomponents/mcstas2/components/CMakeLists.txt)
add_subdirectory(packages)
add_subdirectory(instruments)

# rule to build mcstas components
# this one use distutils and can only run in series
add_custom_target(
  wrap-mcstas-components-serial
  ${EXPORT_ENVVARS};EXPORT_ROOT=${EXPORT_ROOT};EXPORT_PYTHON=${EXPORT_PYTHON};DV_DIR=${CMAKE_SOURCE_DIR};BOOSTPYTHON_LIBDIR=${Boost_LIBRARY_DIR};BOOSTPYTHON_INCDIR=${BOOST_INCLUDE_DIR} ${EXPORT_BIN}/mcvine-compile-all-mcstas-components
  )
add_custom_target(
  reconfigure-to-include-mcstas-components
  cmake ${CMAKE_SOURCE_DIR} -DDEPLOYMENT_PREFIX=${DEPLOYMENT_PREFIX} -DCMAKE_INSTALL_PREFIX=${CMAKE_INSTALL_PREFIX}
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
add_dependencies(reconfigure-to-include-mcstas-components src-for-mcstas-components)
# add_custom_target(
#   wrap-mcstas-components
#  make wrap-mcstas-components-cmake
#  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
#  DEPENDS reconfigure-to-include-mcstas-components
#  )

# install headers 
install (
  DIRECTORY ${EXPORT_HEADERS}/
  DESTINATION include
  )
# install python modules 
install(DIRECTORY ${EXPORT_PYTHON}/
  DESTINATION ${INSTALL_PY_PATH}
  FILES_MATCHING PATTERN "*.py" PATTERN "*.so"
  )
# install exes
install(DIRECTORY ${EXPORT_BIN}/ DESTINATION bin 
  FILES_MATCHING
  PATTERN "*" PERMISSIONS OWNER_READ OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE
  )
# install etc
install(DIRECTORY ${EXPORT_ETC}/ DESTINATION etc)
# install share
install(DIRECTORY ${EXPORT_SHARE}/ DESTINATION share/${PROJECT_NAME}/)
# install tests
install(DIRECTORY ${TESTS_DIR} DESTINATION share/${PROJECT_NAME}/)

# packaging
set(PKG_NAME "mcvine")
# CPACK
set(CPACK_PACKAGE_VERSION ${VERSION})
# set(CPACK_GENERATOR  "RPM")
set(CPACK_GENERATOR  "DEB")
set(CPACK_PACKAGE_NAME ${PKG_NAME})
set(CPACK_PACKAGE_SUMMARY ${SUMMARY})
set(CPACK_PACKAGE_LICENSE ${LICENSE})
set(CPACK_PACKAGE_RELEASE 0)
set(CPACK_PACKAGE_APP_GROUP ${RPM_APP_GROUP})
set(CPACK_PACKAGE_CONTACT ${AUTHOR})
set(CPACK_PACKAGE_VENDOR ${VENDOR})
set(CPACK_PACKAGING_INSTALL_PREFIX ${CMAKE_INSTALL_PREFIX})
set(CPACK_PACKAGE_FILE_NAME "${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_PACKAGE_RELEASE}.${CMAKE_SYSTEM_PROCESSOR}")
set(CPACK_RPM_PACKAGE_REQUIRES "cmake")
set(CPACK_DEBIAN_PACKAGE_DEPENDS "python python-yaml python-numpy python-psutil python-h5py python-mpi4py libgsl0-dev libboost-python-dev libboost-python1.55.0 pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops")
include(CPack)

# source tar ball
add_custom_command(
  OUTPUT ${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz
  COMMAND git archive --format=tar --prefix=${PKG_NAME}-${CPACK_PACKAGE_VERSION}/ HEAD | gzip -c > ${CMAKE_CURRENT_BINARY_DIR}/${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz
  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
  )
add_custom_target( 
  src_tgz
  DEPENDS ${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz 
  )

# CPack does not have a rule for source rpm
# the following is a way to do that
#
set(RPM_BUILD_DIR rpm_build)
# rpm spec file
configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/rpm.spec.in
  ${CMAKE_CURRENT_BINARY_DIR}/${RPM_BUILD_DIR}/SPECS/${PKG_NAME}.spec )
# rules to build src rpm
set(SRC_RPM ${PKG_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_PACKAGE_RELEASE}.src.rpm)
add_custom_command(
  OUTPUT ${SRC_RPM}
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/BUILD
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/BUILDROOT
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/RPMS
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/SOURCES
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/SPECS
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/SRPMS
  COMMAND ${CMAKE_COMMAND} -E make_directory ${RPM_BUILD_DIR}/tmp
  COMMAND ${CMAKE_COMMAND} -E copy ${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz ${RPM_BUILD_DIR}/SOURCES
  COMMAND rpmbuild -bs --define=\"_topdir ${RPM_BUILD_DIR}\" --buildroot=${RPM_BUILD_DIR}/tmp  ${RPM_BUILD_DIR}/SPECS/${PKG_NAME}.spec
  COMMAND ${CMAKE_COMMAND} -E copy ${RPM_BUILD_DIR}/SRPMS/${SRC_RPM} ${SRC_RPM}
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  DEPENDS src_tgz
  )
add_custom_target( 
  srpm
  DEPENDS ${SRC_RPM}
  )

# docker folder for build and test packaging artifacts
execute_process(
  COMMAND rm -rf docker
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )
execute_process(
  COMMAND git clone https://github.com/danse-inelastic/packaging-use-docker docker
  WORKING_DIRECTORY ${CMAKE_SOURCE_DIR}
  )
add_subdirectory(docker)
