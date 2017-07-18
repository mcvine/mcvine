#!/usr/bin/env python
#

import os, unittest
here = os.path.abspath(os.path.dirname(__file__))

    
class TestCase(unittest.TestCase):

    def test(self):
        "neutron_storage: no neutron saved"
        workdir = 'NeutronStorage-zero-neutrons'
        saved = os.path.abspath('.')
        os.chdir(workdir)
        if os.system('bash test.sh'):
            raise RuntimeError("Failed")
        return

    pass # end of TestCase

if __name__ == "__main__": unittest.main()
    
# End of file 
