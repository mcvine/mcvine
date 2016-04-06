# This is used by docker images to test the mcvine installation
# for example, in builders/docker/ubuntu/14.04-from-packagecloud/test
#
set(PROJECT_NAME "mcvine")
set(VERSION "1.0")

project (${PROJECT_NAME})
cmake_minimum_required (VERSION 2.8.11)

# get cmake_utils
execute_process(
  COMMAND rm -rf cmake_utils
  )
execute_process(
  COMMAND git clone https://github.com/danse-inelastic/cmake_utils
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR}/cmake_utils)
# add include them
include(System) # system info
include(Dirs)   # directory structure
include(TestUtils)

# need python
find_package ( PythonLibs REQUIRED )
find_package ( PythonInterp REQUIRED )

# add python tests
set(EXPORT_ENVVARS "PYTHONPATH=$ENV{PYTHONPATH};LD_LIBRARY_PATH=$ENV{LD_LIBRARY_PATH};MCVINE_DIR=${MCVINE_DIR};PATH=$ENV{PATH}")
# Used to include all tests
# PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR} "mcvine")
# But turns out instrument tests are obsolete, so we have to add
# these subdirs one by one and skip instrument
# PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/instrument "instrument")
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/sampleassembly "sampleassembly")
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/mcni "mcni")
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/mccomposite "mccomposite")
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/mccomponents "mccomponents")
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/mcstas2 "mcstas2")
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/mcvine "mcvine")
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR}/mcvine.instruments "mcvine.instruments")

#
enable_testing()
