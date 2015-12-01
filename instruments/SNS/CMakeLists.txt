#
set(PACKAGE_NAME "SNS")
set (LIB_NAME "${PACKAGE_NAME}")
set (PYPKG_NAME "mcvine.instruments.${PACKAGE_NAME}")

# python
file(
  COPY ${PACKAGE_NAME} 
  DESTINATION ${EXPORT_PYTHON}/mcvine/instruments/
  FILES_MATCHING PATTERN "*.py"
  )

# bin
file(COPY bin/ DESTINATION ${EXPORT_BIN}/
  FILES_MATCHING 
  PATTERN "mcvine-sns*"
  )

# tests
set(BUILD_TESTS_PATH ${TESTS_DIR}/mcvine.instruments/${PACKAGE_NAME})
# copy tests to build
file(COPY tests/ DESTINATION ${BUILD_TESTS_PATH})
# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${BUILD_TESTS_PATH} ${PYPKG_NAME})
