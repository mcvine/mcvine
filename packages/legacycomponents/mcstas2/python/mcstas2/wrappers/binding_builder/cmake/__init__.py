#!/usr/bin/env python


def prepare( binding ):
    """prepare binding source tree with CMakeLists.txt"""
    target = "%s.%s" % (binding.python_package, binding.binding_module)
    python_pkg_rel_path = binding.python_package.replace(".", '/')
    python_sources = ' '.join(binding.python_sources)
    include_dirs = ' '.join(binding.c_includes)
    libs = ' '.join(binding.c_libs)
    libdirs = ' '.join(binding.c_libdirs)
    def define2s(key, val):
        if not val: return "-D%s" % key
        return "-D%s=%s" % (key, val)
    defines = ' '.join([define2s(k,v) for k,v in binding.c_defines])
    binding_name = binding.binding_module
    sources = ' '.join(binding.c_sources)
    headers = ' '.join(binding.c_headers)
    cmake_code = cmake_template % locals()
    import os
    fname = os.path.join(
        os.path.dirname(binding.c_sources[0]), 'CMakeLists.txt')
    open(fname, 'wt').write(cmake_code)
    return


cmake_template = """
set(PYTHON_PKG_REL_PATH %(python_pkg_rel_path)s)
set(PYTHON_SOURCES %(python_sources)s)
set(INCLUDE_DIRS %(include_dirs)s)
set(LIBS %(libs)s)
set(LIBDIRS %(libdirs)s)
set(DEFINES %(defines)s)
set(MOD_NAME %(binding_name)s)
set(SRC_FILES %(sources)s %(headers)s)

# python
# file(
#  COPY ${PYTHON_SOURCES} 
#  DESTINATION ${EXPORT_PYTHON}/${PYTHON_PKG_REL_PATH}
#  )
set(PYTHON_TARGET_DIR ${EXPORT_PYTHON}/${PYTHON_PKG_REL_PATH})
set(PYTHON_TARGETS "")
foreach(pysrc ${PYTHON_SOURCES})
  get_filename_component(fn ${pysrc} NAME)
  add_custom_command(OUTPUT ${PYTHON_TARGET_DIR}/${fn}
    COMMAND ${CMAKE_COMMAND} -E copy ${pysrc} ${PYTHON_TARGET_DIR}/${fn}
    )
  list(APPEND PYTHON_TARGETS "${PYTHON_TARGET_DIR}/${fn}")
endforeach()

# -I  -L  -D
include_directories(${INCLUDE_DIRS})
include_directories(${PYTHON_INCLUDE_DIRS})
link_directories(${LIBDIRS})
add_definitions(${DEFINES})

# compile shared library
add_library(${MOD_NAME} SHARED ${SRC_FILES})
target_link_libraries(${MOD_NAME} ${PYTHON_LIBRARY} ${Boost_LIBRARIES}
  ${LIBS})
set_target_properties(${MOD_NAME} PROPERTIES PREFIX "") # dont need "lib" prefix
set_target_properties(${MOD_NAME} PROPERTIES LIBRARY_OUTPUT_DIRECTORY "${EXPORT_PYTHON}/${PYTHON_PKG_REL_PATH}") # export to python directory
set_target_properties(${MOD_NAME} PROPERTIES SKIP_BUILD_RPATH "ON")

# target to include all targets here
add_custom_target(%(target)s DEPENDS ${PYTHON_TARGETS})
add_dependencies(%(target)s ${MOD_NAME})
# 
add_dependencies(wrap-mcstas-components-cmake %(target)s)
"""

# End of file 
