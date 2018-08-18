# DEVELOPER NOTES:
# !!! Make.mm files in subdir boostpython_binding
# !!! are not yet converted to cmake files.

# ------------- Modify these -------------
set ( SRC_FILES 
  geometry/testPrinter.cc
  geometry/testArrowIntersector.cc
  geometry/testDilation.cc
  geometry/testLocator.cc
  geometry/testOverlap.cc
  geometry/test_intersect.cc
  geometry/test_intersectTriangle.cc
  mccomposite/testAbstractNeutronScatterer.cc
  mccomposite/testCompositeNeutronScatterer.cc
  mccomposite/testGeometer.cc
  mccomposite/test_neutron_propagation.cc
  mccomposite/testMultipleScattering.cc
  )
# ----------------------------------------

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${PYTHON_INCLUDE_DIRS})
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})

# compile executable
set(link_libs
  ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${GSL_LIBRARIES}
  "journal" "danse_ins_bpext"
  "-lmcni" "-l${LIB_NAME}"
  )
set(deps ${LIB_NAME})
CUNITTEST_ADD_TESTS(
  "lib${PACKAGE_NAME}" link_libs deps
  ${SRC_FILES})


#
add_subdirectory(boostpython_binding/neutron_printer2)
