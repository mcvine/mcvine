# ------------- Modify these -------------
set ( SRC_FILES 
  Component.cc
  Gravity.cc
  assert.cc
  detector_outputs.cc
  display.cc
  exception.cc
  geometry.cc
  misc.cc
  misc_macros.cc
  propagators.cc
  random_numbers.cc
  tracing_macros.cc
  )
# ----------------------------------------

# include python headers
# include_directories( ${PYTHON_INCLUDE_DIRS} )

# export headers from this project
# file(COPY boostpython_binding mcni_integration
#   DESTINATION ${EXPORT_HEADERS}/mcstas2
#   FILES_MATCHING PATTERN "*.h"
#   )
file(COPY mcstas_compat
  DESTINATION ${EXPORT_HEADERS}/
  FILES_MATCHING PATTERN "*.h"
  )
file(COPY .
  DESTINATION ${EXPORT_HEADERS}/mcstas2 
  FILES_MATCHING PATTERN "*.h"
  )

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${DEPLOYMENT_PREFIX}/include/danse/ins)
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})

# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} )
target_link_libraries(
  ${LIB_NAME} 
  ${PYTHON_LIBRARY} ${Boost_LIBRARIES}
  "journal" "mcni"
  )
set_target_properties(${LIB_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_LIB}") # install to python directory
add_dependencies(${LIB_NAME} "mcni")

# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )

# subdirs
add_subdirectory(share)
