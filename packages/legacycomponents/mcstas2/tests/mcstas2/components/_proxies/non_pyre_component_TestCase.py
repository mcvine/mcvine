#!/usr/bin/env python
#
#


import os, histogram.hdf as hh
import unittest

class TestCase(unittest.TestCase):

    def test(self):
        "mcvine non-pyre interface for monitor"
        ncount = int(1e5)
        buffer_size = int(1e4)
        workdir = 'work-test_source_E_mon'
        cmd = """
        python -m "mcvine.run_script" sim_source_E_mon.py \
            --workdir %s --overwrite_datafiles \
            --ncount %s --buffer_size %s  --mpi-mode server --nodes 1 \
            --run-pps
        """ % (workdir, ncount, buffer_size)
        os.system(cmd)
        IE = hh.load(os.path.join(workdir, 'E.h5'))
        IE_round0 = hh.load(os.path.join(workdir, 'rank0-step0', 'E.h5'))
        total =  IE.I.sum() * ncount
        total_from_round0 = IE_round0.I.sum() * (ncount/buffer_size)
        self.assertAlmostEqual(total/total_from_round0, 1., places=3)
        return

    pass  # end of TestCase


if __name__ == "__main__": unittest.main()
    
# End of file 
