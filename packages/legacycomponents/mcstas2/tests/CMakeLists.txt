#
set(SRC_DIRS 
  lib
  mcstas2bpmodule
  mcstas2
  instruments
  vitess-IO
  # bin
  )

# add c tests
add_subdirectory(lib)

# copy tests directory to build
execute_process(
  COMMAND ${CMAKE_COMMAND} -E copy_directory ${CMAKE_CURRENT_SOURCE_DIR}/ ${TESTS_DIR}/mcstas2/
  )

# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/mcstas2 "mcstas2")
