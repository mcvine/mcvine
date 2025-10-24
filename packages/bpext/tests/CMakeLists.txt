set(SRC_DIRS 
  bpext  
  binding
  )
# establish danse.ins namespace for testing
execute_process(
  COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_BINARY_DIR}/packages/bpext/python/danse/__init__.py
  COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_BINARY_DIR}/packages/bpext/python/danse/ins/__init__.py
)

add_test(NAME signon 
  COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_CURRENT_SOURCE_DIR}/signon.py
  )
set_tests_properties(signon
  PROPERTIES ENVIRONMENT "PYTHONPATH=${CMAKE_BINARY_DIR}/python")


