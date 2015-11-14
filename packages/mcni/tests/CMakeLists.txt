#
set(SRC_DIRS 
  unittestX.py
  mcnimodule
  mcnibpmodule
  mcni
  )

# add c tests
add_subdirectory(libmcni)

# copy tests to build
foreach (_srcdir ${SRC_DIRS})
  file(COPY ${_srcdir} DESTINATION ${TESTS_DIR}/mcni/)
endforeach(_srcdir ${SRC_DIRS})

# add python tests
# PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/mcni "mcni")
# old code to test the macro
# PYUNITTEST_ADD_TEST( ${CMAKE_CURRENT_SOURCE_DIR} "mcvinetest" mcni/neutron_TestCase.py )
