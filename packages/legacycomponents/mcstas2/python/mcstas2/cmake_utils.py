# -*- Python -*-
# Jiao Lin <jiao.lin@gmail.com>
#

import os
#
from .components import componentfactory
from .components.Registry import NotRegisteredError
from .wrappers import createBindingObject
from . import iterComponents, defaultcomponentpath

def create_sources_for_components(path):
    """create source code directories in the given path
    for all components that are not yet wrapped
    This is only to be used as a cmake command.
    See ../../CMakeLists.txt
    """
    for type, category in iterComponents():
        bypass = True
        try:
            f = componentfactory( category, type )
        except NotRegisteredError:
            bypass = False
        else:
            # don't by pass if the source code is newer
            componentpath = defaultcomponentpath( category, type )
            componentsrcdir = os.path.join(path, component_src_subdir(category, type))
            if os.path.exists(componentsrcdir) and \
               os.path.getmtime(componentsrcdir) < os.path.getmtime(componentpath):
                bypass = False
                import shutil
                shutil.rmtree(componentsrcdir)
        if not bypass: 
            create_sources_for_a_component(category, type, path)
        continue
    return


def component_src_subdir(category, type):
    """name of the subdir of component source to be generated
    """
    return '%s_%s' % (category, type)


def create_sources_for_a_component(category, type, path):
    """Do the following:
    * create a source code directory in the given path
      for given component that are not yet wrapped.
    * Add cmake machinery to that directory.
    * Include the directory on the parent directory cmake rule.
    
    This is only to be used as a cmake command.
    See ../../CMakeLists.txt

    path is the root directory of all components, not the individual component
    (../../components)

    """
    componentfn = defaultcomponentpath( category, type )
    directory = component_src_subdir(category, type)
    srcpath = os.path.join(path, directory)
    bindingobj, classname, componentcategory, componentname = \
        createBindingObject(componentfn, category, path=srcpath)
    # add cmake machineries
    from .wrappers.binding_builder import cmake
    cmake.prepare(bindingobj)
    # update components cmakefile
    root_cmakefile = os.path.join(path, 'CMakeLists.txt')
    if not os.path.exists(root_cmakefile) \
       or not open(root_cmakefile).read().strip():
        _init_components_cmakefile(root_cmakefile)
    root_cmake_stream = open(root_cmakefile, 'a+')
    content = root_cmake_stream.read().split('\n')
    line = "add_subdirectory(%s)" % directory
    if line not in content:
        root_cmake_stream.write(line+'\n')
    return


def _init_components_cmakefile(path):
    """initialize the cmakefile of the root of components dir
    """
    root_cmake_stream = open(path, 'wt')
    _w = root_cmake_stream.write
    _w('add_custom_target(wrap-mcstas-components-cmake)\n')
    _w('add_dependencies(wrap-mcstas-components-cmake reconfigure-to-include-mcstas-components)\n')
    root_cmake_stream.close()
    return


# End of file
