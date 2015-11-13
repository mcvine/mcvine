#
set(PACKAGE_NAME "mccomposite")

set (LIB_NAME "${PACKAGE_NAME}")
set (PKG_NAME "${PACKAGE_NAME}")

# 
add_subdirectory(lib)
add_subdirectory(mccompositebpmodule)
add_subdirectory(python)
# add_subdirectory(tests)
