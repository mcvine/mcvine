#
set(SRC_DIRS 
  unittestX.py
  libmccomponents
  mccomponentsbpmodule
  mccomponents
  kernels
  data
  # bin
  )

# add c tests
add_subdirectory(libmccomponents)

# copy tests to build
foreach (_srcdir ${SRC_DIRS})
  file(COPY ${_srcdir} DESTINATION ${TESTS_DIR}/mccomponents/
    FILES_MATCHING 
    PATTERN "*"
    PATTERN "sansmodel*" EXCLUDE)
endforeach(_srcdir ${SRC_DIRS})

# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${TESTS_DIR}/mccomponents "mccomponents")
