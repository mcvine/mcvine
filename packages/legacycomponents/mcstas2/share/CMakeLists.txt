# ------------- Modify these -------------
# ----------------------------------------

# copy share files
file(COPY ./
  DESTINATION ${EXPORT_SHARE}/mcstas2/
  FILES_MATCHING PATTERN "*.comp"
  )
