# ------------- Modify these -------------
set ( SRC_FILES 
  mccomposite/AbstractNeutronScatterer.cc
  mccomposite/CompositeNeutronScatterer.cc
  mccomposite/CompositeNeutronScatterer_Impl.cc
  geometry/visitors/Arrow.cc
  geometry/visitors/ArrowIntersector.cc
  geometry/primitives/Box.cc
  geometry/primitives/Cylinder.cc
  geometry/primitives/Pyramid.cc
  geometry/primitives/Cone.cc
  geometry/visitors/Locator.cc
  geometry/visitors/BoundingBoxMaker.cc
  geometry/primitives/Sphere.cc
  geometry/visitors/Printer.cc
  geometry/intersect.cc
  geometry/locate.cc
  geometry/overlap.cc
  mccomposite/neutron_propagation.cc
  geometry/shape2ostream.cc
  )
# ----------------------------------------

# include python headers
include_directories( ${PYTHON_INCLUDE_DIRS} )

# export headers from this project
file(COPY boostpython_binding geometry
  DESTINATION ${EXPORT_HEADERS}/mccomposite FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")
file(COPY mccomposite/
  DESTINATION ${EXPORT_HEADERS}/mccomposite FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")
file(COPY headers/
  DESTINATION ${EXPORT_HEADERS}/mccomposite FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})
# compile shared lib
add_library ( ${LIB_NAME} SHARED ${SRC_FILES} )
target_link_libraries(${LIB_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} "mcni")
set_target_properties(${LIB_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_LIB}") # install to python directory
add_dependencies(${LIB_NAME} "mcni")

# install shared lib
install (TARGETS ${LIB_NAME}
  LIBRARY DESTINATION ${INSTALL_LIB_DIR}
  )
