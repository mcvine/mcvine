# ------------- Modify these -------------
set ( SRC_FILES 
  _${PYBINDING_NAME}.cc
  bindings.cc
  dblarr.cc
  exceptions.cc
  misc.cc
  register_converters.cc
  )
# ----------------------------------------

# alias
set ( MOD_NAME _${PYBINDING_NAME} )

# -I and -L
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${CMAKE_BINARY_DIR}/packages/bpext/lib/include)
link_directories(${CMAKE_BINARY_DIR}/packages/bpext/lib)

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${LIB_NAME})
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/${PKG_NAME}") # install to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")