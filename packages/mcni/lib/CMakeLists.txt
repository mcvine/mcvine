# ------------- Modify these -------------
set ( SRC_FILES 
  test/exception.cc \
  geometry/Vector3.cc \
  neutron/Event.cc \
  neutron/EventBuffer.cc \
  neutron/Spin.cc \
  neutron/State.cc \
  neutron/Ceventbuffer.cc \
  mcni/process_neutron_events.cc \
  neutron/coords_transform.cc \
  neutron/event_cevent_conversion.cc \
  neutron/units_conversion.cc \
  mcni/AbstractNeutronScatterer.cc \
  )

set ( INC_FILES
  )

set ( EXPORT_HEADERS ${INC_FILES} )
# ----------------------------------------

# include python headers
include_directories( ${PYTHON_INCLUDE_DIRS} )

# export headers from this project
foreach (header ${EXPORT_HEADERS})
  configure_file(
    "${header}"
    "${CMAKE_CURRENT_BINARY_DIR}/include/${PROJECT_NAME}/${header}"
    )
endforeach (header)

# create empty portinfo (pyre-config thing)
execute_process(
  COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_BINARY_DIR}/lib/include/portinfo
)

# -I and -L
include_directories(${CMAKE_BINARY_DIR}/lib/include)
# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} ${INC_FILES} )

# install headers
install (
  DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/include/${PROJECT_NAME}/
  DESTINATION include/${PROJECT_NAME})
# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )
