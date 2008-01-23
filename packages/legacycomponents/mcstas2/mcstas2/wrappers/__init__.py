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
          buildername = 'mm'):

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

    # generate c++ sources for the component
    from component2cppClass.component2cppClass import component2cppClass
    klass = component2cppClass( componentfilename )
    from mcstas2.utils.mills.cxx.factory import createHHandCC
    hh, cc = createHHandCC( klass, path )

    # generate bindings for the c++ class
    from binding import binding
    bindingsources = binding( bindingtype ).generate_binding_sources(
        bindingname, klass, path )

    # build binding
    from binding_builder.Binding import Binding
    binding = Binding(
        python_package = pythonpackage, binding_module = bindingname,
        c_headers = [ hh ],
        c_sources = bindingsources['c'] + [cc],
        python_sources = bindingsources['python'],
        c_libs = ['mcstas2', 'mcni' ],
        c_includes = [ "$(BOOSTPYTHON_INCDIR)" ],
        )
    from binding_builder import builder
    builder( buildername ).build( binding )
        
    # register the new factory
    from mcstas2.components import registercomponent
    m = __import__( '%s.%s' % (pythonpackage, klass.name), {}, {}, [''] )
    registercomponent( componentcategory, componentname, m )
    return 


# version
__id__ = "$Id$"

# End of file 
