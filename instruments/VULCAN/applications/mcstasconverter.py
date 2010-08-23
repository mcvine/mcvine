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

"""
McStasConverter - converts McStas component to the McVine component

Example:

McStas component:

COMPONENT L_monitor9 = L_monitor(
    nchan = 140, filename = "Vulcan_asbuilt_L_monitor9.txt",
    xwidth = 0.15, yheight = 0.15, Lmin = 0.0, Lmax = 14.0,
    restore_neutron = 1)
  AT (0, 0, 0.971)  RELATIVE  FU_Out
  ROTATED (0,ROT,0) relative arm

is converted to:

{"name":        "L_monitor9",
"type":         "L_monitor",
"position":     "AT (0, 0, 0.971)  RELATIVE  FU_Out",
"rotation":     "ROTATED (0,ROT,0) relative arm",
"extra":        [], # like ROTATION
"parameters": {	"nchan": "140",
		"filename": "'Vulcan_asbuilt_L_monitor9.txt'",
		"xwidth": "0.15",
		"yheight": "0.15",
		"Lmin": "0.0",
		"Lmax": "14.0",
		"restore_neutron": "1"}
}

Issues:
    - Check if name is case sensitive (like COMPONENT)
    - Extract properties from "extra" to separate properties
    - Components should at least be separated by "\n\n"
    - Assumption is made that new line is "\n"
"""

tempText = """COMPONENT L_monitor9 = L_monitor(
    nchan = 140, filename = "Vulcan_asbuilt_L_monitor9.txt",
    xwidth = 0.15, yheight = 0.15, Lmin = 0.0, Lmax = 14.0,
    restore_neutron = 1)
  AT (0, 0, 0.971)  RELATIVE  FU_Out
  ROTATED (0,ROT,0) relative arm
  hello world

  """

# Imports
import re

# Regular expressions
SPACES          = '[ \t]*'              # Spaces and tabs
NAME            = '%s([^ ()=]*)%s' % (SPACES, SPACES)  # Extracts name
NO_BRACKETS     = '[^()]*'              # No brackets
PARAMETERS      = '(%s)' % NO_BRACKETS  # Component parameters
COMPONENT       = "COMPONENT%s=%s\(%s\)(.*)\n\n" %(NAME, NAME, PARAMETERS)  # Component

# Constants
PROPERTIES      = ["AT", "ROTATED"]     # Standard properties

# Utils
ifelse  = lambda a,b,c: (b,c)[not a]    # C ternary operator '?:'

class McStasConverter:

    def __init__(self, filename, parse=False):
        self._filename      = filename
        self._components    = []    # list of dictionaries


    def parse(self):
        "Parses file content and appends component to self._components"

        # Remove comments
        p   = re.compile(COMPONENT, re.DOTALL)
        matches     = p.findall(tempText)       # Finds all components

        for m in matches:
            comp    = {}
            comp["name"]        = m[0]
            comp["type"]        = m[1]
            comp["parameters"]  = self._params(m[2])
            comp["position"]    = self._position(m[3])
            comp["rotation"]    = self._rotation(m[3])
            comp["extra"]       = self._extra(m[3])

            self._components.append(comp)


    def components(self):
        "Returns list of components"
        return self._components


    def _params(self, text):
        "Returns dictionary of parameters"
        if not text:
            return {}   # Empty dictionary

        text    = self._removeComments(text)
        plist   = text.split(",")
        params  = {}
        for pp in plist:
            keyval  = pp.split("=")
            assert len(keyval) == 2
            name            = keyval[0].strip()
            value           = keyval[1].strip()
            params[name]    = value

        return params


    # XXX
    def _removeComments(self, text):
        "Removes comments from the text"
        return text


    def _position(self, text):
        "Extracts position from text"
        return self._property("AT", text)


    def _rotation(self, text):
        "Extracts rotation from text"
        return self._property("ROTATED", text)


    def _extra(self, text):
        "Return list of extra properies that are not in property list"
        extra   = []
        if not text:
            return extra

        props   = self._properties(text)
        for key in props.keys():
            if not key in PROPERTIES:
                extra.append(props[key])
                
        return extra


    def _property(self, key, text):
        "Takes key and returns property from text as a string"
        # Example: 'AT (0, 0, 0.971)  RELATIVE  FU_Out'
        if not key or not text:
            return ""

        props   = self._properties(text)
        value   = props.get(key.upper())
        return ifelse(value, value, "")


    def _properties(self, text):
        "Returns dictionary of properties with the first word as the key"
        # Example: {'AT': 'AT (0, 0, 0.971)  RELATIVE  FU_Out',}
        prop   = {}

        if not text:
            return prop
        
        tl    = text.split("\n")    # Split properies by empty line
        for t in tl:
            kv  = self._propKeyValue(t)
            if not kv:
                continue    # No key-value tuple

            prop[kv[0]]    = kv[1]

        return prop


    def _propKeyValue(self, line):
        "Takes line, tries to extract the first word and returns (key, value) or None - otherwise"
        if not line:
            return None

        line    = line.strip()
        parts   = line.split(" ")
        first   = parts[0]      # First word
        if first == "":
            return None

        key     = first.upper()
        return (key, line)


    # XXX: Fix
    def toString(self, indent=4, br="\n"):
        #print self._params("hi")
        print self._components


if __name__ == "__main__":
    conv    = McStasConverter("hi")
    conv.parse()
    conv.toString()

__date__ = "$Aug 19, 2010 10:25:18 AM$"


