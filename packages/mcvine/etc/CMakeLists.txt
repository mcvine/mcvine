# ------------- Modify these -------------
# ----------------------------------------

# install
install(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/
  DESTINATION etc/${PKG_NAME}
  FILES_MATCHING PATTERN "*.pml"
  )
