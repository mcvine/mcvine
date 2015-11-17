# ------------- Modify these -------------
set ( LIB_NAME mcstas2_share )
set ( SRC_FILES 
  read_table-lib.cc
  monitor_nd-lib.cc
  )
# ----------------------------------------

# include python headers
# include_directories( ${PYTHON_INCLUDE_DIRS} )

# export headers from this project
# file(COPY ./
#  DESTINATION ${EXPORT_HEADERS}/mcstas2/share/
#  FILES_MATCHING PATTERN "*.h"
#  )

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})

# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} )
# target_link_libraries(${LIB_NAME})
set_target_properties(${LIB_NAME} 
  PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_LIB}"
  ) # install to lib directory

# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )


