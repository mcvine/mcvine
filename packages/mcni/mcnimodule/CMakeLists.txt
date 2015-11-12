# ------------- Modify these -------------
set ( SRC_FILES 
  _${PYBINDING_NAME}.cc
  ProxyDevice.cc
  bindings.cc
  exceptions.cc
  facility.cc
  journal.cc
  misc.cc
  state.cc
  )
# ----------------------------------------

# alias
set ( MOD_NAME _${PYBINDING_NAME} )

# -I and -L
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${CMAKE_BINARY_DIR}/lib/include)
link_directories(${CMAKE_BINARY_DIR}/lib)

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} -l"${LIB_NAME}")
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/python/modules/${PROJECT_NAME}") # install to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")