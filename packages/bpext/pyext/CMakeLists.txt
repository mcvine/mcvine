# ------------- Modify these -------------
set ( SRC_FILES 
  _${PYBINDING_NAME}.cc
  bindings.cc
  dblarr.cc
  exceptions.cc
  misc.cc
  register_converters.cc
  )
# ----------------------------------------

# alias
set ( MOD_NAME _${PYBINDING_NAME} )

# create empty portinfo (pyre-config thing)
file(MAKE_DIRECTORY "${CMAKE_BINARY_DIR}/lib/include/")
# execute_process(
#   COMMAND ${CMAKE_COMMAND} -E touch ${CMAKE_BINARY_DIR}/packages/bpext/lib/include/portinfo
# )
#  message(" \n\n\n -------- PORTINFO --------------" ${PYBINDING_NAME}, ${PKG_NAME} )

# -I and -L
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
include_directories(${CMAKE_BINARY_DIR}/packages/bpext/lib/include)
include_directories(${CMAKE_BINARY_DIR}/packages/bpext/lib/include/danse/ins)
link_directories(${CMAKE_BINARY_DIR}/packages/bpext/lib)

# include_directories(${PYTHON_INCLUDE_DIRS})
# include_directories(${Boost_INCLUDE_DIRS})
# include_directories(${DEPLOYMENT_PREFIX}/lib/include)
# include_directories(${DEPLOYMENT_PREFIX}/lib/include/danse/ins)
# link_directories(${DEPLOYMENT_PREFIX}/lib)

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${LIB_NAME})
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/${PKG_NAME}") # install to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")













# # include python headers
# include_directories( ${PYTHON_INCLUDE_DIRS} )
# include_directories( ${GSL_INCLUDE_DIRS} )

# # export headers from this project
# file(COPY boostpython_binding homogeneous_scatterer kernels physics
#   DESTINATION ${EXPORT_HEADERS}/mccomponents
#   FILES_MATCHING PATTERN "*.h" PATTERN "*.icc"
#   )
# file(COPY math
#   DESTINATION ${EXPORT_HEADERS}/mccomponents 
#   FILES_MATCHING PATTERN "*.h" PATTERN "*.icc"
#   )
# file(COPY headers/
#   DESTINATION ${EXPORT_HEADERS}/mccomponents FILES_MATCHING PATTERN "*.h" PATTERN "*.icc")

# # -I and -L
# include_directories(${EXPORT_HEADERS})
# include_directories(${DEPLOYMENT_PREFIX}/include)
# link_directories(${EXPORT_LIB})
# link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})
# add_definitions(-DUSE_DANSE_NAMESPACE)

# # fparser
# add_subdirectory("math/fparser-${FPARSER_VERSION}")

# # compile shared lib
# add_library ( ${LIB_NAME} SHARED ${SRC_FILES} )
# target_link_libraries(
#   ${LIB_NAME} 
#   ${PYTHON_LIBRARY} ${Boost_LIBRARIES} ${GSL_LIBRARIES}
#   "mcni" "mccomposite" "fparser"
#   )
# set_target_properties(${LIB_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_LIB}") # install to python directory
# add_dependencies(${LIB_NAME} "mccomposite")

# # install shared lib
# install (TARGETS ${LIB_NAME}
#   LIBRARY DESTINATION ${INSTALL_LIB_DIR}
#   )






# # -I and -L
# include_directories(${EXPORT_HEADERS})
# include_directories(${DEPLOYMENT_PREFIX}/include)
# include_directories(${PYTHON_INCLUDE_DIRS})
# include_directories(${Boost_INCLUDE_DIRS})
# link_directories(${EXPORT_LIB})
# link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})

# # compile shared library
# add_library(${MOD_NAME} SHARED ${SRC_FILES})
# target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} "mcpl" ${LIB_NAME})
# set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
# set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/${PKG_NAME}") # export to python directory
# set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")
# add_dependencies(${MOD_NAME} ${LIB_NAME})
