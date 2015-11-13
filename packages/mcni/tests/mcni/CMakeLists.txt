#

# Extract the test by running python code 

execute_process(COMMAND "python" ${LIST_PYTESTS_PY} 
  OUTPUT_VARIABLE STR_TESTS
  OUTPUT_STRIP_TRAILING_WHITESPACE
  ERROR_STRIP_TRAILING_WHITESPACE)

separate_arguments(TEST_LIST UNIX_COMMAND ${STR_TESTS})

foreach(ATEST ${TEST_LIST})
    #message(" +")
    #message(${ATEST})

    add_test(${ATEST} "python" "-m" "unittest" "-v" ${ATEST})

endforeach(ATEST)
