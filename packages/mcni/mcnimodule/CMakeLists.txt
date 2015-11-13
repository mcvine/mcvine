# ------------- Modify these -------------
set (PYBINDING_NAME "${PACKAGE_NAME}module")
set ( SRC_FILES 
  ${PYBINDING_NAME}.cc
  bindings.cc
  exceptions.cc
  misc.cc
  register_bp_voidptr_converters.cc
  )
# ----------------------------------------

# alias
set ( MOD_NAME ${PYBINDING_NAME} )

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${PYTHON_INCLUDE_DIRS})
link_directories(${EXPORT_LIB})

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} -l"${LIB_NAME}")
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/${PKG_NAME}") # export to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")
