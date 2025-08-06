# ------------- Modify these -------------
set (PYBINDING_NAME "${PACKAGE_NAME}bp")
set ( SRC_FILES 
  ${PYBINDING_NAME}.cc
  wrap_basics.cc
  wrap_AbstractShape.cc
  wrap_shapecontainer.cc
  wrap_geometers.cc
  wrap_primitives.cc
  wrap_operations.cc
  wrap_scatterercontainer.cc
  wrap_shapeoperators.cc
  wrap_AbstractNeutronScatterer.cc
  wrap_CompositeNeutronScatterer.cc
  )
# ----------------------------------------

# alias
set ( MOD_NAME ${PYBINDING_NAME} )

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} "mcni" ${LIB_NAME})
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/${PKG_NAME}") # export to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")
add_dependencies(${MOD_NAME} ${LIB_NAME})
