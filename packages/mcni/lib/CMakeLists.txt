# ------------- Modify these -------------
set ( SRC_FILES 
  test/exception.cc
  geometry/Vector3.cc
  neutron/Event.cc
  neutron/EventBuffer.cc
  neutron/Spin.cc
  neutron/State.cc
  neutron/Ceventbuffer.cc
  mcni/process_neutron_events.cc
  neutron/coords_transform.cc
  neutron/event_cevent_conversion.cc
  neutron/units_conversion.cc
  mcni/AbstractNeutronScatterer.cc
  )
# ----------------------------------------

# include python headers
include_directories( ${PYTHON_INCLUDE_DIRS} )

# export headers from this project
file(COPY boostpython_binding geometry math neutron test
  DESTINATION include/mcni FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")
file(COPY mcni/
  DESTINATION include/mcni FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")
file(COPY headers/
  DESTINATION include/mcni FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")

# -I and -L
include_directories(${CMAKE_CURRENT_BINARY_DIR}/include)
include_directories(${DEPLOYMENT_PREFIX}/include)
# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} )

# install headers
install (
  DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/include/${PACKAGE_NAME}/
  DESTINATION include/${PACKAGE_NAME})
# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )
