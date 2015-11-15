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

# copy tests to build
foreach (_srcdir ${SRC_DIRS})
  file(COPY ${_srcdir} DESTINATION ${TESTS_DIR}/mcstas2/)
endforeach(_srcdir ${SRC_DIRS})

# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/mcstas2 "mcstas2")
