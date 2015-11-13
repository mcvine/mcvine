# ------------- Modify these -------------
# ----------------------------------------

# not needed any more

# copy all python source over to build directory
file(COPY ${PKG_NAME} DESTINATION "modules/")

# install
install(DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/modules/
  DESTINATION ${INSTALL_PY_PATH}
  FILES_MATCHING PATTERN "*.py" PATTERN "*.so"
  )
