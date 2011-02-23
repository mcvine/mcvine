#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


DEBUG = False
# DEBUG = True


def componentfactory( category, type ):
    '''obtain component factory method of given category and type
Examples:
  componentfactory( 'monitors', 'E_monitor' )
  '''


def componentinfo( category, type ):
    '''obtain component info of given category and type
Examples:
  componentinfo( 'monitors', 'E_monitor' )
  '''    
    return info


def listallcomponentcategories( ):
    '''list all component categories'''
    return uniquelist( defaultcategories + categoriesinregistry )


def listcomponentsincategory( category ):
    return uniquelist( defaultcomponents + registered )


# version
__id__ = "$Id$"

# End of file 
