# ------------- Modify these -------------
# ----------------------------------------

# copy all python source over to build directory
file(COPY ${PKG_NAME} DESTINATION ${EXPORT_PYTHON}/
  FILES_MATCHING PATTERN "*.py")

# create version.py
execute_process(
  COMMAND ${PYTHON_EXECUTABLE} ${CMAKE_BINARY_DIR}/cmake_utils/create_version_py.py "# mcvine version" ${CMAKE_SOURCE_DIR} ${EXPORT_PYTHON}/${PKG_NAME}/version.py
  )
