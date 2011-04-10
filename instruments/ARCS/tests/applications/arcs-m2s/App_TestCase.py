#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#



def execute(cmd):
    import subprocess as sp
    p = sp.Popen(cmd, shell=True, stdout=sp.PIPE, stderr=sp.PIPE)
    out, err = p.communicate()
    if p.wait():
        raise RuntimeError, "%s failed.\nOUT:%s\nERR:%s\n" % (
            cmd, out, err)
    return out, err


import unittest
class TestCase(unittest.TestCase):

    def test1(self):
        cmd = 'arcs-m2s --dry_run'
        out, err = execute(cmd)
        argv = eval(out.splitlines()[-1])
        # print argv
        self.assert_('-fermichopper=fermichopper-100-1.5-SMI' in argv)
        self.assert_('-fermichopper.nu=600.0' in argv)
        self.assert_('-fermichopper.tc=0.00317317948677' in argv)
        for arg in argv:
            self.assert_(not arg.startswith('-fermichopper.blader'))
        return


    def test2(self):
        cmd = 'arcs-m2s --dry_run --fermi_bladeradius=3.'
        out, err = execute(cmd)
        argv = eval(out.splitlines()[-1])
        # print argv
        self.assert_('-fermichopper=fermichopper-100-1.5-SMI' in argv)
        self.assert_('-fermichopper.nu=600.0' in argv)
        self.assert_('-fermichopper.tc=0.00317317948677' in argv)
        self.assert_('-fermichopper.blader=3.0' in argv)
        return


    def test3(self):
        cmd = 'arcs-m2s --dry_run --fermi_chopper=700-0.5-AST'
        out, err = execute(cmd)
        argv = eval(out.splitlines()[-1])
        # print argv
        self.assert_('-fermichopper=fermichopper-700-0.5-AST' in argv)
        self.assert_('-fermichopper.nu=600.0' in argv)
        self.assert_('-fermichopper.tc=0.00317317948677' in argv)
        for arg in argv:
            self.assert_(not arg.startswith('-fermichopper.blader'))
        return


    def test4(self):
        cmd = 'arcs-m2s --dry_run --fermi_chopper=700-0.5-AST --fermi_bladeradius=3.'
        out, err = execute(cmd)
        argv = eval(out.splitlines()[-1])
        # print argv
        self.assert_('-fermichopper=fermichopper-700-0.5-AST' in argv)
        self.assert_('-fermichopper.nu=600.0' in argv)
        self.assert_('-fermichopper.tc=0.00317317948677' in argv)
        self.assert_('-fermichopper.blader=3.0' in argv)
        return


    pass  # end of TestCase



def pysuite():
    suite1 = unittest.makeSuite(TestCase)
    return unittest.TestSuite( (suite1,) )


def main(): unittest.main()
if __name__ == "__main__":
    main()
    
# version
__id__ = "$Id: detectorcomponent_TestCase.py 855 2011-02-09 16:41:24Z linjiao $"

# End of file 