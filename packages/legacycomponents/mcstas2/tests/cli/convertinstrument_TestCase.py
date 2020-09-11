#!/usr/bin/env python
#

import os, unittest

here = os.path.abspath(os.path.dirname(__file__) or '.')

class mcstas_parser_TestCase(unittest.TestCase):

    def test1(self):
        instr = os.path.join(here, 'simple.instr')
        import tempfile
        d = tempfile.mkdtemp(dir=here, prefix='tmp_convertinstrument')
        cmd = 'cd %s; mcvine mcstas convertinstrument %s' % (d, instr)
        self.assertTrue(os.system(cmd)==0)
        cmd = 'diff expected/non-pyre/simple_mcvine.py %s/simple_mcvine.py' % d
        self.assertTrue(os.system(cmd)==0)
        import shutil
        shutil.rmtree(d)
        return
    
    def test2(self):
        instr = os.path.join(here, 'simple.instr')
        import tempfile
        d = tempfile.mkdtemp(dir=here, prefix='tmp_convertinstrument')
        cmd = 'cd %s; mcvine mcstas convertinstrument %s --type=pyre' % (d, instr)
        self.assertTrue(os.system(cmd)==0)
        cmd = 'diff expected/pyre %s' % d
        self.assertTrue(os.system(cmd)==0)
        import shutil
        shutil.rmtree(d)
        return
    
    pass

if __name__ == "__main__":
    unittest.main()
    
# End of file
