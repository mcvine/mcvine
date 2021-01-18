#!/usr/bin/env python
#

import os, unittest, json

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
        # non pyre
        cmd = 'cd %s; mcvine mcstas convertinstrument %s --type=pyre' % (d, instr)
        self.assertTrue(os.system(cmd)==0)
        # pyre
        for fn in os.listdir('expected/pyre'):
            if fn.startswith('.'): continue
            p = os.path.join('expected/pyre', fn)
            if fn.endswith('.json'):
                with open(p) as stream:
                    expected_data = json.load(stream)
                with open(os.path.join(d, fn)) as stream:
                    data = json.load(stream)
                self.assertEqual(data, expected_data)
            else:
                cmd = 'diff expected/pyre/%s %s/%s' % (fn, d, fn)
                self.assertEqual(os.system(cmd), 0)
        import shutil
        shutil.rmtree(d)
        return
    
    pass

if __name__ == "__main__":
    unittest.main()
    
# End of file
