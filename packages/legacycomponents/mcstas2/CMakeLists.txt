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
