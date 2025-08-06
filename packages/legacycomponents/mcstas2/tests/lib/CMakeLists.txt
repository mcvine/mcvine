# ------------- Modify these -------------
set ( SRC_FILES 
  testGravity
  testComponent
  test_detector_output_macros
  test_random_numbers
  )
# ----------------------------------------

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${PYTHON_INCLUDE_DIRS})
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})

# add tests
set(link_libs
  ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${GSL_LIBRARIES}
  "-lmcni" "-l${LIB_NAME}"
  )
set(deps ${LIB_NAME})
CUNITTEST_ADD_TESTS(
  "lib${PACKAGE_NAME}" link_libs deps
  ${SRC_FILES})


