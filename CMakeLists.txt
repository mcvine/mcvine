# To improve
# * dependency items are declared at different places
#   - This file 
#     - DOCKER_PKGING_DEPS_DEB: deb pkgs needed in building and installation 
#     - DOCKER_PKGING_DEPS_RPM: rpm pkgs needed in building and installation. should be the same as DOCKER_PKGING_DEPS_DEB except the name might be somewhat different. for example, numpy is called python-numpy in ubuntu, but just numpy in fedora
#     - CPACK_DEBIAN_PACKAGE_DEPENDS: deb pkgs needed during installation only
#   - File rpm.spec.in:
#     - BuildRequires: rpm pkgs needed during build
#     - Requires: rpm pkgs needed during installation
# * rpm and deb releases are treated differently:
#   - rpm: source rpm
#   - deb: binary deb
#
# conda build instructions
# $ conda install anaconda-client # for upload conda pkg to anaconda
# $ conda config --set anaconda_upload yes # for automatic upload
# $ conda config --add channels conda-forge # conda-forge provides gsl
# $ conda config --add channels mcvine # mcvine provides danse pkgs
# $ conda update -n root conda-build # tool for building conda pkg
# $ make conda-build-pkg
# additional conda cmds
# remove mcvine pkg from anaconda site for mcvine
# $ anaconda remove mcvine/mcvine/1.0.1/linux-64/mcvine-1.0.1-py27_0.tar.bz2
# upload pkg to anaconda site
# $ anaconda upload /home/lj7/anaconda2/conda-bld/linux-64/mcvine-1.0.1-py27_0.tar.bz2

set(PROJECT_NAME "mcvine")
set(VERSION "1.3")
set(AUTHOR "Jiao Lin")
set(AUTHOR_EMAILE "jiao.lin@gmail.com")
set(VENDOR "DANSE")
set(SUMMARY "Monte Carlo VIrtual Neutron Experiment")
set(LICENSE "BSD")
set(RPM_APP_GROUP "Development/Tools")
set(GITHUB_URL "https://github.com/mcvine/mcvine")
# can change this to a branch or a tag, for example
# set(GIT_RELEASE_TAG ${VERSION})
set(GIT_RELEASE_TAG "v1.1-alpha")
set (HOMEPAGE ${GITHUB_URL})

# Is this still needed?
# this is released with danse.ins packages
# set(DEP_DANSE_PKGS "pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops")

# packaging with the help of docker and packagecloud
# package repository at packagecloud
set (PKGCLOUD_USERNAME "danse")
set (PKGCLOUD_REPO "ins")
# dependencies
set (DOCKER_PKGING_DEPS_DEB "python-yaml python-numpy python-psutil python-h5py python-mpi4py libgsl0-dev libboost-python-dev libboost-python1.55.0 pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops mcvine-resources")
set (DOCKER_PKGING_DEPS_RPM "python-yaml numpy python-psutil h5py mpi4py-mpich2 gsl-devel boost-devel boost-python pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops mcvine-resources")
set (DOCKER_PKGING_TEST_SRPM ". /opt/danse/bin/setup-danse.sh && mcvine")
set (DOCKER_PKGING_BUILDSTEP_BUILDCMD "cd .. && git clone https://github.com/mcvine/resources.git &&  /work/src/builders/build /work/src /work/build /opt/danse /work/resources")
set (DOCKER_PKGING_TEST_RPM ${DOCKER_PKGING_TEST_SRPM})
set (DOCKER_PKGING_TEST_DEB ${DOCKER_PKGING_TEST_SRPM})
set (VERSION_FOR_CONDA_PKGING 1.1alpha)
set (CONDA_PKGING_BUILD_DEPS "python pyyaml numpy psutil h5py mpi4py gsl boost pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops mcvine-resources")
set (CONDA_PKGING_RUN_DEPS "python pyyaml numpy psutil h5py mpi4py gsl boost pyre danse.ins.dsm danse.ins.numpyext danse.ins.bpext histogram danse.ins.matter drchops mcvine-resources")
set(CONDA_BUILD_MAKE_CMD "cmake -DCMAKE_INSTALL_PREFIX=$PREFIX -DDEPLOYMENT_PREFIX=$PREFIX .. && make -j $CORES && make -j$CORES reconfigure-to-include-mcstas-components && make -j$CORES wrap-mcstas-components-cmake && make -j$CORES && make install")

#
project (${PROJECT_NAME})
cmake_minimum_required (VERSION 2.8.11)

# get cmake_utils
IF(EXISTS "cmake_utils/")
  execute_process(
    COMMAND git pull
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/cmake_utils
    )
ELSE(EXISTS "cmake_utils/")
  execute_process(
    COMMAND git clone https://github.com/danse-inelastic/cmake_utils
    WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
    )
ENDIF(EXISTS "cmake_utils/")
set(CMAKE_MODULE_PATH ${PROJECT_BINARY_DIR}/cmake_utils)

# use utils
include(System) # system info
include(Dirs)   # directory structure
# customize the env vars for the testing environment
set(EXPORT_ENVVARS "PYTHONPATH=${EXPORT_PYTHON}:$ENV{PYTHONPATH};LD_LIBRARY_PATH=${EXPORT_LIB}:$ENV{LD_LIBRARY_PATH};MCVINE_DIR=${EXPORT_ROOT};PATH=${EXPORT_BIN}:$ENV{PATH};EXPORT_ROOT=${EXPORT_ROOT};MCVINE_WORKFLOW=${EXPORT_ROOT}/share/workflow")
include(TestUtils)
# message("lib: $ENV{LD_LIBRARY_PATH}; python: $ENV{PYTHONPATH}")

# needs python
find_package ( PythonLibs REQUIRED )
find_package ( PythonInterp REQUIRED )
# python installation path
set(INSTALL_PY_PATH "${INSTALL_LIB_DIR}/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages")
# needs boost python
find_package ( Boost COMPONENTS python )
message(" - Boost lib and header dirs: ${Boost_LIBRARY_DIRS} ${Boost_INCLUDE_DIRS}")
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
  ${EXPORT_ENVVARS};EXPORT_ROOT=${EXPORT_ROOT};EXPORT_PYTHON=${EXPORT_PYTHON};DV_DIR=${CMAKE_SOURCE_DIR};BOOSTPYTHON_LIBDIR=${Boost_LIBRARY_DIR};BOOSTPYTHON_INCDIR=${Boost_INCLUDE_DIR} ${EXPORT_BIN}/mcvine-compile-all-mcstas-components
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
install(DIRECTORY ${EXPORT_SHARE}/ DESTINATION share/${PROJECT_NAME}/ USE_SOURCE_PERMISSIONS)
# install tests
install(DIRECTORY ${TESTS_DIR} DESTINATION share/${PROJECT_NAME}/ USE_SOURCE_PERMISSIONS)
# install top level cmake file and script for tests
install(FILES builders/runtests/CMakeLists.txt DESTINATION share/${PROJECT_NAME}/tests/)
install(PROGRAMS builders/runtests/test.py DESTINATION share/${PROJECT_NAME}/tests/)

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
set(CPACK_DEBIAN_PACKAGE_DEPENDS "python, python-yaml, python-numpy, python-psutil, python-h5py, python-mpi4py, libgsl0-dev, libboost-python-dev, libboost-python1.55.0, pyre, danse.ins.dsm, danse.ins.numpyext, danse.ins.bpext, histogram, danse.ins.matter, drchops, mcvine-resources")
include(CPack)

# source tar ball
set(SOURCE_TARBALL_WORKDIR ${CMAKE_CURRENT_BINARY_DIR}/src-tarball)
execute_process(
  COMMAND mkdir -p ${SOURCE_TARBALL_WORKDIR}
)
add_custom_command(
  OUTPUT ${SOURCE_TARBALL_WORKDIR}/${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz
  COMMAND git clone ${GITHUB_URL} ${PKG_NAME}-${CPACK_PACKAGE_VERSION} && tar cfz ${SOURCE_TARBALL_WORKDIR}/${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz ${PKG_NAME}-${CPACK_PACKAGE_VERSION}
  WORKING_DIRECTORY ${SOURCE_TARBALL_WORKDIR}
  )
add_custom_target( 
  src_tgz
  DEPENDS ${SOURCE_TARBALL_WORKDIR}/${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz 
  )

# CPack does not have a rule for source rpm
# the following is a way to do that
#
set(RPM_BUILD_DIR rpm_build)
# rpm spec file
set(RPM_SPEC_IN "rpm.spec.in")
configure_file( ${CMAKE_CURRENT_SOURCE_DIR}/${RPM_SPEC_IN}
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
  COMMAND ${CMAKE_COMMAND} -E copy ${SOURCE_TARBALL_WORKDIR}/${PKG_NAME}-${CPACK_PACKAGE_VERSION}.tar.gz ${RPM_BUILD_DIR}/SOURCES
  COMMAND rpmbuild -bs --define=\"_topdir ${RPM_BUILD_DIR}\" --buildroot=${RPM_BUILD_DIR}/tmp  ${RPM_BUILD_DIR}/SPECS/${PKG_NAME}.spec
  COMMAND ${CMAKE_COMMAND} -E copy ${RPM_BUILD_DIR}/SRPMS/${SRC_RPM} ${SRC_RPM}
  WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
  DEPENDS src_tgz
  )
add_custom_target( 
  srpm
  DEPENDS ${SRC_RPM}
  )

# folders for build and test packaging artifacts
# deb/rpm
include(docker)
# conda
include(conda)
set(CONDA_TEST_SCRIPT "run_test.py")
configure_file(builders/runtests/test.py conda/run_test.py)
