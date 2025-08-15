#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com
#

standalone = True

import unittest, os


class TestCase(unittest.TestCase):


    def test(self):
        'mcni.pyre_support: parallel app'
        from mcni.pyre_support.MpiApplication \
            import mpi_launcher_choice as launcher
        cmd = "python parallel_app.py --%(launcher)s.nodes=2" % locals()
        print(cmd)
        if os.system(cmd):
            raise RuntimeError("%s failed" % cmd)
        return
    
        
    pass  # end of TestCase


def main():
    unittest.main()
    return


if __name__ == "__main__": main()
    
# End of file 
