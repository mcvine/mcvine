# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                               Alex Dementsov
#                      California Institute of Technology
#                        (C) 2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

import unittest
from mcstasconverter import McStasConverter
import fixtures

class mcstas_converter_TestCase(unittest.TestCase):

    def setUp(self):
        self.conv    = McStasConverter(filename="vanadium_example.instr")


    def test_components_num(self):
        components  = self.conv.components()
        self.assertEqual(len(components), 6)


    def test_component_first(self):
        first   = self.conv.components()[0]
        self.assertEqual(first["name"], "arm")
        self.assertEqual(first["type"], "Arm")
        self.assertEqual(first["position"], "AT (0,0,0) ABSOLUTE")
        self.assertEqual(first["rotation"], "")
        self.assertEqual(first["extra"], [])
        self.assertEqual(first["parameters"], {})


    def test_component_rotation(self):
        five    = self.conv.components()[4]
        self.assertEqual(five["position"], "AT (0,0,0) RELATIVE target")
        self.assertEqual(five["rotation"], "ROTATED (0,ROT,0) relative arm")

        
    def test_component_params(self):
        six     = self.conv.components()[5]
        params  = six["parameters"]
        self.assertEqual(len(params), 4)
        self.assertEqual(params["nx"], "101")
        self.assertEqual(params["ny"], "51")
        self.assertEqual(params["radius"], "10")
        self.assertEqual(params["filename"], '"vanadium.psd"')


class mcstas_converter_config_TestCase(unittest.TestCase):

    def setUp(self):
        self.conv    = McStasConverter(config=fixtures.textMain)

    def test_component_num(self):
        self.assertEqual(len(self.conv.components()), 2)
        

    def test_component_first(self):
        first   = self.conv.components()[0]
        self.assertEqual(first["name"], "L_monitor9")
        self.assertEqual(first["type"], "L_monitor")
        self.assertEqual(first["position"], "AT (0, 0, 0.971)  RELATIVE  FU_Out")
        self.assertEqual(first["rotation"], "ROTATED (0,ROT,0) relative arm")
        self.assertEqual(first["extra"], [])


    def test_component_params(self):
        # Test some parameters
        first   = self.conv.components()[0]
        params  = first["parameters"]
        self.assertEqual(len(params), 7)
        self.assertEqual(params["nchan"], "140")
        self.assertEqual(params["yheight"], "0.15")
        self.assertEqual(params["filename"], '"Vulcan_asbuilt_L_monitor9.txt"')


if __name__ == "__main__":
    unittest.main()

__date__ = "$Aug 22, 2010 8:45:09 PM$"


