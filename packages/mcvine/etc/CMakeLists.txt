# ------------- Modify these -------------
# ----------------------------------------

# copy etc files
file(COPY ${CMAKE_CURRENT_SOURCE_DIR}/
  DESTINATION ${EXPORT_ETC}/
  FILES_MATCHING PATTERN "*.pml"
  )

