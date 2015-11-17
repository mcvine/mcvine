# ------------- Modify these -------------
# ----------------------------------------

# copy all python source over to build directory
file(COPY ${PKG_NAME} DESTINATION ${EXPORT_PYTHON}/
  FILES_MATCHING PATTERN "*.py")
