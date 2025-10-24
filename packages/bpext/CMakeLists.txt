# cmake_minimum_required (VERSION 3.5)
# project (bpext)

# set(VERSION "0.1")
# set(AUTHOR "Jiao Lin")
# set(AUTHOR_EMAILE "jiao.lin@gmail.com")
# set(VENDOR "DANSE")
# set(SUMMARY "danse.ins utils for working with Boost Python library")
# set(LICENSE "BSD")
# set(RPM_APP_GROUP "Development/Tools")
# set(GITHUB_URL "https://github.com/danse-inelastic/bpext")
# set (HOMEPAGE ${GITHUB_URL})


# # variables
set (PYBINDING_NAME "bpext")
set (LIB_NAME "bpext")
set (PARENT_PATH "")
# set (PARENT_PY_PKG "")
# set (PARENT_GITHUB_URL "https://github.com/danse-inelastic/danse.ins")
# set (PARENT_VERSION "0.1")
# set (PARENT_RELEASE "0")
set (PKG_NAME "bpext")


# # get cmake_utils
# IF(EXISTS "cmake_utils/")
#   execute_process(
#     COMMAND git pull
#     WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/cmake_utils
#     )
# ELSE(EXISTS "cmake_utils/")
#   execute_process(
#     COMMAND git clone https://github.com/danse-inelastic/cmake_utils
#     WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
#     )
# ENDIF(EXISTS "cmake_utils/")
# set(CMAKE_MODULE_PATH ${PROJECT_BINARY_DIR}/cmake_utils)


# # lib64
# #include(System)

# # ABI
# add_definitions(-D_GLIBCXX_USE_CXX11_ABI=0)

# #list(APPEND CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}")

# # needs python
# find_package ( PythonLibs REQUIRED )
# find_package ( PythonInterp REQUIRED )
# # python installation path
# set(INSTALL_PY_PATH "${INSTALL_LIB_DIR}/python${PYTHON_VERSION_MAJOR}.${PYTHON_VERSION_MINOR}/site-packages")

# # needs boost python
# # find_package ( Boost REQUIRED )
# # find_package ( BoostPython REQUIRED )
# set(PYVER_MAJORMINOR ${PYTHON_VERSION_MAJOR}${PYTHON_VERSION_MINOR})
# find_package ( Boost COMPONENTS python${PYVER_MAJORMINOR} )
# IF (NOT Boost_FOUND)
#    find_package ( Boost COMPONENTS python${PYTHON_VERSION_MAJOR} )
# ENDIF (NOT Boost_FOUND)
# IF (NOT Boost_FOUND)
#    find_package ( Boost COMPONENTS python REQUIRED )
# ENDIF (NOT Boost_FOUND)

# #
# enable_testing()

# # subdirs
# add_subdirectory(lib)
# add_subdirectory(pyext)
# add_subdirectory(_examplebpbinding)
# add_subdirectory(python)
# add_subdirectory(tests)

set(PACKAGE_NAME "bpext")

# set (LIB_NAME "${PACKAGE_NAME}")
# set (PKG_NAME "${PACKAGE_NAME}")

# 
# subdirs
add_subdirectory(lib)
add_subdirectory(pyext)
add_subdirectory(_examplebpbinding)
add_subdirectory(python)
add_subdirectory(tests) 
