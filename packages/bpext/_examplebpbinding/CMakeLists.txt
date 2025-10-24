# ------------- Modify these -------------
set ( SRC_FILES 
  _examplebpbindingmodule.cc
  wrap.cc
  )
# ----------------------------------------

# alias
set ( MOD_NAME _examplebpbinding )

# -I and -L
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${CMAKE_BINARY_DIR}/lib/include/)
# link_directories(${Boost_LIBRARY_DIRS})
link_directories(${CMAKE_BINARY_DIR}/lib)

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${LIB_NAME})
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/bpext") # install to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")

# copy all python source over to build directory
file(COPY ${MOD_NAME} DESTINATION ${EXPORT_PYTHON}/bpext
  FILES_MATCHING PATTERN "*.py")


message(" -------- \n _examplebpbinding \n -------------- " ${EXPORT_PYTHON})

