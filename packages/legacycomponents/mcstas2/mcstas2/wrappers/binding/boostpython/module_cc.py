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

#Generate <name>module.cc

template = '''
#include <boost/python.hpp>


void wrap();


BOOST_PYTHON_MODULE(%s)
{
  using namespace boost::python;
  wrap();
}


'''

def generate( name, path ):
    content = template % name
    import os
    filename = os.path.join( path, "%smodule.cc" % name )
    open(filename, 'w').write( content )
    return filename


# version
__id__ = "$Id$"


# End of file 
