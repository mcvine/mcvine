#
set(PACKAGE_NAME "mcstas2")

set (LIB_NAME "${PACKAGE_NAME}")
set (PKG_NAME "${PACKAGE_NAME}")

find_package(GSL REQUIRED)

# 
add_subdirectory(lib)
add_subdirectory(mcstas2bpmodule)
add_subdirectory(python)
add_subdirectory(tests)
add_subdirectory(share)

# bin
file(COPY bin/ DESTINATION ${EXPORT_BIN}/ 
  FILES_MATCHING PATTERN "mcvine*")

add_subdirectory(components)
add_custom_target(
  src-for-mcstas-components
  ${EXPORT_ENVVARS};EXPORT_ROOT=${EXPORT_ROOT};EXPORT_PYTHON=${EXPORT_PYTHON};DV_DIR=${CMAKE_SOURCE_DIR};BOOSTPYTHON_LIBDIR=${Boost_LIBRARY_DIR};BOOSTPYTHON_INCDIR=${BOOST_INCLUDE_DIR} python -c \"import mcstas2 as m2\; m2.create_sources_for_components('${CMAKE_SOURCE_DIR}/packages/legacycomponents/mcstas2/components')\"
  )
