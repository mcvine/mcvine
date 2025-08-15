#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#


skip = True


import unittestX as unittest

import mcni


class TestCase(unittest.TestCase):


    def test1(self):
        from dos import loadDOS
        dos = loadDOS()
        E = dos.energy; g = dos.I
        import pylab
        pylab.plot(E, g)
        pylab.show()
        from mccomponents.sample.phonon.utils import fitparabolic
        E, g = fitparabolic(E,g)
        pylab.plot(E,g)
        pylab.show()
        return


    def test2(self):
        from mccomponents.sample.idf import readDOS
        e,Z = readDOS('./graphite-DOS')
        from mccomponents.sample.phonon.utils import nice_dos
        nice_dos(e,Z, force_fitparabolic=True)
        return
        
        
    pass  # end of TestCase


def main(): unittest.main()
    
    
if __name__ == "__main__": main()
    
# End of file 
