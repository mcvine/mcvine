# -*- Python -*-
#

import os, unittest

here = os.path.abspath(os.path.dirname(__file__) or '.')

class mcstas_parser_TestCase(unittest.TestCase):

    def test1(self):
        instr = os.path.join(here, 'simple.instr')
        import tempfile
        d = tempfile.mkdtemp(dir=here, prefix='tmp_convertinstrument')
        cmd = 'cd %s; mcvine mcstas convertinstrument %s' % (d, instr)
        self.assert_(os.system(cmd)==0)
        import shutil
        shutil.rmtree(d)
        return
    
    pass

if __name__ == "__main__":
    unittest.main()
    
# End of file
