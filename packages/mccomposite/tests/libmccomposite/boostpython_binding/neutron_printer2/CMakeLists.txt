#
set (PACKAGE_NAME "neutron_printer2")
set (PYPKG_NAME "${PACKAGE_NAME}")
set (PYBINDING_NAME "${PACKAGE_NAME}bpmodule")
set (MOD_NAME ${PYBINDING_NAME} )
set ( SRC_FILES 
  ${PYBINDING_NAME}.cc
  wrap.cc
  )

# python
file(
  COPY ./
  DESTINATION ${EXPORT_PYTHON}/
  FILES_MATCHING PATTERN "*.py"
  )

# -I and -L
include_directories(${EXPORT_HEADERS})
include_directories(${DEPLOYMENT_PREFIX}/include)
include_directories(${PYTHON_INCLUDE_DIRS})
include_directories(${Boost_INCLUDE_DIRS})
link_directories(${EXPORT_LIB})
link_directories(${DEPLOYMENT_PREFIX}/${INSTALL_LIB_DIR})

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES} "journal" "mcni" "mccomposite")
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/") # export to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")
add_dependencies(${MOD_NAME} "mccomposite")
