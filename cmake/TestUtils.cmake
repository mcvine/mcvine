macro ( PYUNITTEST_ADD_TEST _test_src_dir _testname_prefix )
  # Add all of the individual tests so that they can be run in parallel
  foreach ( part ${ARGN} )
    # message( ${part} )
    get_filename_component( _filename ${part} NAME )
    get_filename_component( _suitename ${part} NAME_WE )
    get_filename_component( _directory ${part} DIRECTORY )
    string(SUBSTRING ${_directory} 1 -1 _dir) # remove the leading "."
    set ( _pyunit_separate_name "${_testname_prefix}${_dir}/${_suitename}" )
    # message( "name: ${_pyunit_separate_name}, cmd:${PYTHON_EXECUTABLE} -B ${_filename}, workdir:  ${_test_src_dir}/${_directory}" )
    add_test ( NAME ${_pyunit_separate_name}
      COMMAND ${PYTHON_EXECUTABLE} -B ${_filename} )
    set_tests_properties ( ${_pyunit_separate_name} PROPERTIES 
      WORKING_DIRECTORY ${_test_src_dir}/${_directory}
      ENVIRONMENT PATH="${EXPORT_BIN}:$ENV{PATH}"
      ENVIRONMENT PYTHONPATH="${EXPORT_PYTHON}:$ENV{PYTHONPATH}"
      ENVIRONMENT LD_LIBRARY_PATH="${EXPORT_LIB}:$ENV{LD_LIBRARY_PATH}"
      )
  endforeach ( part ${ARGN} )
endmacro ( PYUNITTEST_ADD_TEST )

macro ( PYUNITTEST_ADD_TESTS_IN_DIR _test_src_dir _testname_prefix)
  execute_process(
    COMMAND find . -name *TestCase.py
    WORKING_DIRECTORY ${_test_src_dir}
    OUTPUT_VARIABLE _tests
    )
  separate_arguments(_testlist UNIX_COMMAND ${_tests})
  # message( ${_testlist} )
  PYUNITTEST_ADD_TEST( ${_test_src_dir} ${_testname_prefix} ${_testlist} )
endmacro ( PYUNITTEST_ADD_TESTS_IN_DIR )
