set(SRC_DIRS 
  unittestX.py
  bpext  
  binding
  )
# establish danse.ins namespace for testing
# execute_process(
#   COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_BINARY_DIR}/packages/bpext/python/danse/__init__.py
#   COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_BINARY_DIR}/packages/bpext/python/danse/ins/__init__.py
# )


# copy tests to build
foreach (_srcdir ${SRC_DIRS})
  file(COPY ${_srcdir} DESTINATION ${TESTS_DIR}/bpext/)
endforeach(_srcdir ${SRC_DIRS})

#signon.py test missing
# add_test(NAME signon 
#   COMMAND ${PYTHON_EXECUTABLE} ${TESTS_DIR}/bpext/signon.py
#   )
# set_tests_properties(signon
#   PROPERTIES ENVIRONMENT "PYTHONPATH=${CMAKE_BINARY_DIR}/python")


# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/bpext "bpext")