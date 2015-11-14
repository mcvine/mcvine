# DEVELOPER NOTES:
# !!! Make.mm files in subdir boostpython_binding
# !!! are not yet converted to cmake files.

# ------------- Modify these -------------
set ( SRC_FILES 
  geometry/testPrinter.cc
  geometry/testArrowIntersector.cc
  geometry/testDilation.cc
  geometry/testLocator.cc
  geometry/test_intersect.cc
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
foreach( _src ${SRC_FILES} )
  get_filename_component( _filename ${_src} NAME )
  get_filename_component( _exe ${_src} NAME_WE )
  get_filename_component( _directory ${_src} DIRECTORY )
  set(_target_path ${_directory}/${_exe})
  string(REPLACE "/" "_" _target_name ${_target_path})
  file(MAKE_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}/${_directory})
  add_executable(${_target_name} ${_src})
  target_link_libraries(
    ${_target_name} ${PYTHON_LIBRARY} ${Boost_LIBRARIES}
    "journal" "danse_ins_bpext" "mcni" -l"${LIB_NAME}"
    )
  set(_testname ${_src})
  add_test(
    NAME lib${PACKAGE_NAME}/${_testname} 
    COMMAND ${_target_name}
    WORKING_DIRECTORY ${CMAKE_CURRENT_BINARY_DIR}
    )
endforeach( _src ${SRC_FILES} ) 

