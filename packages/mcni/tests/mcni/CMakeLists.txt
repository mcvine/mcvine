#

# Extract the test by running python code 

# execute_process(
#  COMMAND python ${LIST_PYTESTS_PY} "." "*TestCase.py"
#  WORKING_DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}
#  OUTPUT_VARIABLE STR_TESTS
#  OUTPUT_STRIP_TRAILING_WHITESPACE
#  ERROR_STRIP_TRAILING_WHITESPACE
#  )

# message("${STR_TESTS}")
# separate_arguments(TEST_LIST UNIX_COMMAND ${STR_TESTS})

# foreach(ATEST ${TEST_LIST})
#  message(" +")
#  message(${ATEST})
#  add_test(${ATEST} "python" "-m" "unittest" "-v" ${ATEST})
#endforeach(ATEST)

# PYUNITTEST_ADD_TEST( ${CMAKE_CURRENT_SOURCE_DIR} "mcvinetest" neutron_TestCase.py )
PYUNITTEST_ADD_TESTS_IN_DIR( ${CMAKE_CURRENT_SOURCE_DIR} "mcni")