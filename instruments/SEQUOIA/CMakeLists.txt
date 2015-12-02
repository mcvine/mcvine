#
set(PACKAGE_NAME "SEQUOIA")
set (LIB_NAME "${PACKAGE_NAME}")
set (PYPKG_NAME "mcvine.instruments.${PACKAGE_NAME}")

# python
file(
  COPY ${PACKAGE_NAME} 
  DESTINATION ${EXPORT_PYTHON}/mcvine/instruments/
  FILES_MATCHING PATTERN "*.py"
  )

# etc
file(COPY etc/
  DESTINATION ${EXPORT_ETC}/
  FILES_MATCHING PATTERN "*.pml" PATTERN "*.odb"
  )

# app
file(COPY applications/ DESTINATION ${EXPORT_BIN}/
  FILES_MATCHING PATTERN "sequoia*"
  )

# tests
set(BUILD_TESTS_PATH ${TESTS_DIR}/mcvine.instruments/${PACKAGE_NAME})
# copy tests to build
file(COPY tests/ DESTINATION ${BUILD_TESTS_PATH})
# add python tests
PYUNITTEST_ADD_TESTS_IN_DIR( ${BUILD_TESTS_PATH} ${PYPKG_NAME})
