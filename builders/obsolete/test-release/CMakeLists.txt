# This file should be added to the root of the "tests"
# directory which are installed on /opt/danse/share/mcvine/tests
# Then 
#  . /opt/danse/bin/setup-danse.sh
#  mkdir -p /work/test-mcvine
#  cd /work/test-mcvine
#  cmake /opt/danse/share/mcvine/tests
#  make test ARGS="-j 10"

cmake_minimum_required(VERSION 2.8)

enable_testing()

find_package ( PythonInterp REQUIRED )

get cmake_utils
execute_process(
  COMMAND rm -rf cmake_utils
  )
execute_process(
  COMMAND git clone https://github.com/danse-inelastic/cmake_utils
  WORKING_DIRECTORY ${CMAKE_BINARY_DIR}
  )
set(CMAKE_MODULE_PATH ${PROJECT_BINARY_DIR}/cmake_utils)

#
include(TestUtils)
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_SOURCE_DIR} "mcvine")
