# fparser

set(LIB_NAME fparser)
set(SRC_FILES
  fparser.cc
  fpoptimizer.cc
  )

file(COPY ./
  DESTINATION ${EXPORT_HEADERS}/fparser/
  FILES_MATCHING PATTERN "*.hh"
  )

# -I and -L
# include_directories(${EXPORT_HEADERS})
# include_directories(${DEPLOYMENT_PREFIX}/include)
# link_directories(${EXPORT_LIB})
# link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})


# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} )
# target_link_libraries(${LIB_NAME})
set_target_properties(${LIB_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_LIB}") # install to lib export

# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )
