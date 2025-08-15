#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

from __future__ import print_function

standalone = True


import unittestX as unittest


scattererxml = 'scatterers/fccNi/Ni-scatterer-SQEkernel.xml'


class scattererxml_TestCase(unittest.TestCase):


    def test1(self):
        'mccomponents.sample.kernelxml.parser'
        from mccomponents.sample.kernelxml import parse_file
        scatterer = parse_file( scattererxml )

        kernel = scatterer.kernel()
        self.assertTrue( isKernel( kernel ) )
        return
    

    def test2(self):
        'mccomponents.sample.kernelxml.renderer'
        
        sqehisth5 = 'sqehist.h5'
        outputs = [sqehisth5]
        _remove( outputs )
        
        from mccomponents.sample.kernelxml import parse_file, render
        scatterer = parse_file( scattererxml )
        
        renderedxml = "%s.rendered" % scattererxml
        print('\n'.join(render(scatterer)), file=open(renderedxml,'w'))

        scatterer1 = parse_file( renderedxml )
        return
    

    pass  # end of scattererxml_TestCase


def _remove( files ):
    import os
    for path in files:
        if os.path.exists( path ):
            if not os.path.isfile(path):
                raise IOError("%s is not a file" % path)
            os.remove( path )
            pass
        continue
    return


def isKernel(candidate):
    from mccomponents.homogeneous_scatterer.Kernel import Kernel
    return isinstance(candidate, Kernel)


def pysuite():
    suite1 = unittest.makeSuite(scattererxml_TestCase)
    return unittest.TestSuite( (suite1,) )


def main(): unittest.main()

    
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id$"

# End of file 
