#
set(SRC_DIRS 
  unittestX.py
  mccompositebpmodule
  mccomposite
  )

# add c tests
add_subdirectory(libmccomposite)

# copy tests to build
foreach (_srcdir ${SRC_DIRS})
  file(COPY ${_srcdir} DESTINATION ${TESTS_DIR}/mccomposite/)
endforeach(_srcdir ${SRC_DIRS})

# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/mccomposite "mccomposite")
