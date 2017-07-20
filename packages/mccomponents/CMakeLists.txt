#
set(PACKAGE_NAME "mccomponents")

set (LIB_NAME "${PACKAGE_NAME}")
set (PKG_NAME "${PACKAGE_NAME}")

# 
add_subdirectory(lib)
add_subdirectory(mccomponentsbpmodule)
add_subdirectory(python)
add_subdirectory(tests)
add_subdirectory(bin)
