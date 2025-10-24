# ------------- Modify these -------------
set ( SRC_FILES 
  extractor_registry.cc
  wrapper_registry.cc
  )

set ( INC_FILES
  bpext.h
  extractor_registry.h
  wrapper_registry.h
  extract_ptr.h
  wrap_ptr.h
  WrappedPointer.h
  )

set ( EXPORT_HEADERS_F
  bpext.h
  extractor_registry.h
  wrapper_registry.h
  extract_ptr.h
  wrap_ptr.h
  WrappedPointer.h
  
  )
# ----------------------------------------

# include python headers
include_directories( ${PYTHON_INCLUDE_DIRS} )

# export headers from this project
foreach (header ${EXPORT_HEADERS_F})
  configure_file(
    "${header}"
    "${CMAKE_BINARY_DIR}/export/include/bpext/${header}"
    )
endforeach (header)
#"${CMAKE_CURRENT_BINARY_DIR}/include/${PARENT_PATH}/bpext/${header}"


configure_file(
  "portinfo"
  "${CMAKE_BINARY_DIR}/export/include/bpext/portinfo"
  )

# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} ${INC_FILES} )
  
target_include_directories(${LIB_NAME}
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_BINARY_DIR}/export/include>  # build tree headers
        $<INSTALL_INTERFACE:include>                            # installed headers
)
  


# install headers
install (
  DIRECTORY ${CMAKE_BINARY_DIR}/export/include/bpext
  DESTINATION include/bpext)

  message(" \n\n\n -------- CMkaje list --------------" ${CMAKE_BINARY_DIR}/export/include/bpext)
# # install shared lib
# install (TARGETS ${LIB_NAME}
#   LIBRARY DESTINATION ${INSTALL_LIB_DIR}
#   )


message(" -------- \n CMAKE_CURRENT_BINARY_DIR \n -------------- " ${CMAKE_CURRENT_SOURCE_DIR})


# # export headers from this project
# file(COPY   bpext  extractor_registry   wrapper_registry   extract_ptr  wrap_ptr  WrappedPointer
#   DESTINATION ${EXPORT_HEADERS}/bpext FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")



# compile shared lib
# add_library ( ${LIB_NAME} SHARED ${SRC_FILES} ${INC_FILES} )
#target_link_libraries(${LIB_NAME} "bpext")
set_target_properties(${LIB_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_LIB}") # install to python directory


# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )

# -I and -L
include_directories(${EXPORT_HEADERS_F})
include_directories(${DEPLOYMENT_PREFIX}/include)  