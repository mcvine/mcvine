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


## toolsets to create python bindings.
## A binding is described as an instance of Binding.Binding class.
## A subpackage here describes a toolset to build bindings.
## Every subpackage must define a method "build", which
## takes a binding instance as the only argument.
##


def builder( name ):
    exec 'import %s as package' % name
    #package = __import__(name, {}, {},  [])
    return package


# version
__id__ = "$Id$"

# End of file 
