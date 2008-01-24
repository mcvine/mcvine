#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


def wrap( componentfilename, componentcategory,
          pythonpackage = None,
          path = None, componentname = None,
          bindingname = None, bindingtype = 'boostpython',
          buildername = 'mm', pythonexportroot = None):
    """wrap a McStas component in python
  componentfilename: component file path. Eg. /.../monitors/E_monitor.comp
  componentcategory: category of component. Eg. monitors
  pythonpackage: the python package where this component will be export to. Eg. mcstas.components.monitors
  path: temporary path where binding sources go
  componentname: name of the component. Eg. E_monitor
  bindingname: name of the binding. Eg. E_monitorboostpython
  bindingtype: type of binding. Eg. boostpython (currently only this is supported)
  buildername: binding builder. choices: mm and distutils
  pythonexportroot: directory where python modules are exported. Eg. $EXPORT_ROOT. None means pyton modules will be exported wherever the binding builder's default export path.
  
    """

    if pythonpackage is None:
        pythonpackage = 'mcstas2.components.%s' % componentcategory
        pass
    
    if not path:
        import temporaryfiles
        path = temporaryfiles.temporarydir()
        pass

    if not componentname:
        import os
        componentname = os.path.splitext( os.path.basename( componentfilename ) )[0]
        pass

    if not bindingname: bindingname = '%s%s' % (componentname, bindingtype)

    # read component info
    from mcstas2.utils.parsers import parseComponent
    compInfo = parseComponent( componentfilename )

    # generate c++ sources for the component
    from component2cppClass.component2cppClass import componentInfo2cppClass
    klass = componentInfo2cppClass( compInfo )
    from mcstas2.utils.mills.cxx.factory import createHHandCC
    hh, cc = createHHandCC( klass, path )

    # generate bindings for the c++ class
    from binding import binding
    bindingsources = binding( bindingtype ).generate_binding_sources(
        bindingname, klass, path )

    # genearte python code to wrap the binding into a factory method
    from pymodule import generate
    pysources = generate( compInfo, klass, bindingname, path ) 
    if bindingsources.get( 'python' ) is None:
        bindingsources['python'] = pysources
    else:
        bindingsources['python'] += pysources

    # build binding
    from binding_builder import binding
    binding = binding(
        python_package = pythonpackage, binding_module = bindingname,
        c_headers = [ hh ],
        c_sources = bindingsources['c'] + [cc],
        python_sources = bindingsources['python'],
        c_libs = ['mcstas2', 'mcni' ],
        c_includes = [ ],
        dependencies = [ bindingtype, 'caltech-config', 'mcstas2', 'mcni' ],
        )
    from binding_builder import builder
    builder( buildername ).build( binding, pythonexportroot )
    
    # register the new factory
    from mcstas2.components import registercomponent
    m = __import__( '%s.%s' % (pythonpackage, klass.name), {}, {}, [''] )
    registercomponent( componentcategory, componentname, m )
    return 


# version
__id__ = "$Id$"

# End of file 
