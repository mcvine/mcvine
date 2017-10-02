#!/usr/bin/env python

from mcvine.instruments.SEQUOIA import moderator as mod
import numpy as np

import unittest

class TestCase(unittest.TestCase):
    def test_emission_time(self):
        assert np.isclose(mod.estimate_emission_time(700.), 1.64957304642e-06)
        return


if __name__ == '__main__': unittest.main()
