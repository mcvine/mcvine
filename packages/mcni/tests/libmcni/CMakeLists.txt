# DEVELOPER NOTES:
# !!! Make.mm files in subdir boostpython_binding
# !!! are not yet converted to cmake files.

# ------------- Modify these -------------
set ( SRC_FILES 
  neutron/testEvent.cc
  geometry/testVector3.cc
  geometry/testMatrix3.cc
  geometry/testcoords_transform.cc
  geometry/testutils.cc
  mcni/testAbstractNeutronScatterer.cc
  mcni/testAbstractNeutronComponent.cc
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
  "bpext"
  "-l${LIB_NAME}"
  )
set(deps ${LIB_NAME})
CUNITTEST_ADD_TESTS(
  "lib${PACKAGE_NAME}" link_libs deps
  ${SRC_FILES})
