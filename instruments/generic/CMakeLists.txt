#
set(PACKAGE_NAME "generic")
set (LIB_NAME "${PACKAGE_NAME}")
set (PYPKG_NAME "mcvine.instruments.${PACKAGE_NAME}")

# etc
file(COPY etc/
  DESTINATION ${EXPORT_ETC}/
  FILES_MATCHING PATTERN "*.pml" PATTERN "*.odb"
  )

# app
file(COPY applications/ DESTINATION ${EXPORT_BIN}/
  FILES_MATCHING
  PATTERN "*.py"
  PATTERN "mcvine*"
  )

