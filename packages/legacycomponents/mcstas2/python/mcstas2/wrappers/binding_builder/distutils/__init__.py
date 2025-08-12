#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


import os


def build( binding, site_package_path = None ):
    '''
    binding: the binding to build
    site_package_path: the path to which the built binding will be installed.
      if None, installed to /.../site-pacakges
    '''
    python_package = binding.python_package
    binding_module = binding.binding_module
    c_headers = binding.c_headers
    c_sources = binding.c_sources
    python_sources = binding.python_sources
    c_libs = binding.c_libs
    c_libdirs = binding.c_libdirs
    if 'boost_python' in c_libs: _find_boostpython_lib(c_libs, c_libdirs)
    c_includes = binding.c_includes
    c_defines = binding.c_defines
    
    from distutils.core import setup, Extension
    ext = Extension(
        '%s.%s' % (python_package, binding_module ),
        c_sources,# + c_headers,
        include_dirs = c_includes,
        libraries = c_libs,
        library_dirs = c_libdirs,
        define_macros = c_defines,
        )

    if len(python_sources):
        # need to make sure all python sources come from the same directory
        import os
        pysrcdir = os.path.split( python_sources[0] ) [0]
        for module in python_sources:
            if os.path.split( module )[0] != pysrcdir:
                raise "not all python sources in the same directory: %s" %(
                    python_sources, )
            continue

        package_dir = { python_package: pysrcdir }
    else:
        package_dir = {}
        pass


    import sys
    save = sys.argv
    sys.argv = ['', 'install']
    if site_package_path: sys.argv.append( '--install-lib=%s' % site_package_path )


    name = python_package.split( '.' )[0]
    packages = [python_package]
    ext_modules = [ext]
    record_path = os.path.expanduser("~/.mcstas2/install_record.txt")
    sys.argv.append( '--single-version-externally-managed')
    sys.argv.append( '--record' )
    sys.argv.append( record_path )
    setup(
        name = name,
        packages = packages,
        package_dir = package_dir,
        ext_modules = ext_modules,
    )
    import importlib
    importlib.invalidate_caches()
    sys.argv = save
    return


def _find_boostpython_lib(libs, libdirs):
    import sys, glob
    major, minor = sys.version_info[:2]
    pyver = '%s%s' % (major, minor)  # "27" for 2.7
    candidates = 'boost_python%s' % pyver, 'boost_python%s' % major, 'boost_python'
    exts = '.so', '.dylib'
    found = None
    for c in candidates:
        for libdir in libdirs:
            for ext in exts:
                pattern = '%s/lib%s*%s' % (libdir, c, ext)
                files = glob.glob(pattern)
                if files:
                    found=os.path.basename(files[0])[3: -len(ext)]
                    break
                if glob.glob(pattern): found=c; break
            if found: break
        if found: break
    if not found:
        raise RuntimeError("Did not find boostpython library in {}".format(', '.join(libdirs)))
    # modify libs
    libs[libs.index('boost_python')] = found
    return


# version
__id__ = "$Id$"

# End of file 
