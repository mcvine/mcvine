# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                           Alex Dementsov, Jiao Lin
#                      California Institute of Technology
#                        (C) 2010  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
McStasConverter - converter for McStas components to list of dictionaries.
                  This is a convenient form to create other data structures
                  and scripts (e.g. McVine components).

Example:

McStas component

COMPONENT L_monitor9 = L_monitor(
    nchan = 140, filename = "Vulcan_asbuilt_L_monitor9.txt",
    xwidth = 0.15, yheight = 0.15, Lmin = 0.0, Lmax = 14.0,
    restore_neutron = 1)
  AT (0, 0, 0.971)  RELATIVE  FU_Out
  ROTATED (0,ROT,0) relative arm

is converted to dictionary:

{"name":        "L_monitor9"
"type":         "L_monitor"
"position":     "AT (0, 0, 0.971)  RELATIVE  FU_Out"
"rotation":     "ROTATED (0,ROT,0) relative arm"
"extra":        []
"parameters":  {"nchan":          "140"
                "yheight":         "0.15"
                "restore_neutron": "1"
                "filename":        "\"Vulcan_asbuilt_L_monitor9.txt\""
                "Lmax":            "14.0"
                "xwidth":          "0.15"
                "Lmin":            "0.0"
                }
}

Notes:
    - Options are case non-sensitive
    - "Relative <COMP>" means relative to the nearest to source component
    - Position format:
        AT (x, y, z) RELATIVE <Name>
        AT (x, y, z) ABSOLUTE
        AT (x, y, z) RELATIVE PREVIOUS

    - Rotation format:
        ROTATED (Ax, Ay, Az) RELATIVE <Name>
        ROTATED (Ax, Ay, Az) ABSOLUTE
        AT (x, y, z) RELATIVE PREVIOUS ROTATED (Ax, Ay, Az) RELATIVE PREVIOUS(2) # Not supported

Issues:
    - Does not support 'AT(x,y,z) ...'
    - Check if name is case sensitive (like COMPONENT)
    - Extract properties from "extra" to separate properties
    - Assumption is made that new line is "\n"

"""

# XXX: Fix rotation part in geometer parameter in toMcvineString() (it is not generated correctly)
# XXX: Fix options issue (see fixtures.textOptions)
# XXX: Implement nice align of dictionary entries in toBuilderString()
# XXX: Implement filter for parameters and components
# XXX: Filter is not set correctly (because it does not propagate to methods that use the filter)

# XXX: Fix 
#    _VnfString()
#    _toInstrString()

# Get rid of _absoluteVector()

# Refactoring of position and rotation is in progress

# Imports
import re
import sys
import os.path
from time import localtime, strftime
from mcstas2.utils.parsers.McStasComponentParser import McStasComponentParser
# from compmodules import IMPORT_DICT, PARAMS_DICT, INSTRUMENT, PARAM_FILTER, COMP_FILTER, BUILD_DICT

# Regular expressions
COMMENT         = '(/\*.*?\*/)'         # Non-greedy comment (.*?)
SPACES          = '[ \t]*'              # Spaces and tabs
NAME            = '%s([^ ()=]*)%s' % (SPACES, SPACES)  # Extracts name
NO_BRACKETS     = '[^()]*'              # No brackets
PARAMETERS      = '(%s)' % NO_BRACKETS  # Component parameters
COMPONENT       = "%s=%s\(%s\)(.*)" %(NAME, NAME, PARAMETERS)  # Component
VECVAL          = "([^,\)]+)"             # Vector's value
VECVAL          = "(.*)"             # Vector's value
VECTOR          = "\(%s,%s,%s\)" % (VECVAL, VECVAL, VECVAL) # Vector
VECTOR_F        = "(\([^\)]*\))"
POSITION        = "AT%s%s%s(RELATIVE|ABSOLUTE)%s([^ ]*)" % (SPACES, VECTOR, SPACES, SPACES)
ROTATION        = "ROTATED%s%s%s(RELATIVE|ABSOLUTE)%s([^ ]*)" % (SPACES, VECTOR, SPACES, SPACES)
RELTO           = "to=\"([^\"]+)\"" # Relative to component

# Constants
PROPERTIES      = ["AT", "ROTATED"]     # Standard properties
RELATION        = ["RELATIVE", "ABSOLUTE"]
TERMINATORS     = ["FINALLY", "END"]


# Utils
ifelse  = lambda a,b,c: (b,c)[not a]    # C ternary operator '?:'



class Instrument:

    name = None
    parameters = None
    init = None
    components = None


class Component:

    type = None
    name = None
    parameters = None
    position = None
    orientation = None



class McStasInstrumentParser(object):

    def parse(self, text):
        "Parses text and return a list of component dictionaries"
        #
        instrument = Instrument()
        # Remove comments
        text         = self._removeComments(text)
        compSplits   = text.split("COMPONENT")   # Split by component parts
        header       = compSplits[0]
        # get instrument info
        instrument.name, instrument.parameters, instrument.init = \
            self._parseHeader(header)
        compSplits   = compSplits[1:]             # Skip 0 part (should not have components)

        # Go over the component strings and populate components
        components = []
        for compText in compSplits:
            p   = re.compile(COMPONENT, re.DOTALL)
            # Finds all components (well, there should be one component)
            matches     = p.findall(compText)

            if not matches or not matches[0]: # No match, procede to the next candidate
                continue

            # Populate component
            m = matches[0]
            comp    = Component()
            components.append(comp)

            comp.name        = m[0]
            comp.type        = m[1]
            comp.parameters  = self._params(m[2])
            position = comp.position  = self._position(m[3])
            rotation    = self._rotation(m[3])
            if rotation is None:
                rotation = list(position)
                rotation[0] = (0,0,0)
            comp.orientation = tuple(rotation)
            comp.extra       = m[3]

        instrument.components = components
        return instrument

    
    def _parseHeader(self, header):
        instr_def, b = header.split('DECLARE')
        d, instr_def = instr_def.split('INSTRUMENT')
        assert d.strip() == 'DEFINE'
        p = re.compile('\((.*?)\)', re.DOTALL)
        params = p.findall(instr_def)[0]
        params = ''.join([l.strip() for l in params.strip().splitlines()])
        name, e = instr_def.split('(')
        p = re.compile("INITIALIZE\n%{.*%}", re.DOTALL)
        init = p.findall(b)[0]
        init = '\n'.join(init.splitlines()[2:-1])
        return name, params, init
    

    def _params(self, text):
        "Returns dictionary of parameters"
        if not text:
            return {}   # Empty dictionary

        ctext   = text.strip()      # Can have unnecessary white spaces
        plist   = ctext.split(",")
        params  = {}
        for pp in plist:
            keyval  = pp.split("=")
            if len(keyval) == 2:
                name            = keyval[0].strip()
                value           = keyval[1].strip()
                params[name]    = value

        return params


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
        
        tl    = text.split("\n")        # Split properies by empty line
        for t in tl:
            kv  = self._propKeyValue(t)
            if not kv:
                continue    # No key-value tuple

            if kv[0] in TERMINATORS:    # Terminators found return properties
                return prop
                
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


    def _position(self, text):
        """
        Returns absolute position of component with respect to source

        Example of text: AT (0, 0, 0.39855)  RELATIVE  PREVIOUS
        """
        return self._vectorRelation("AT", "position", POSITION, text)
        

    def _rotation(self, text):
        """
        Returns absolute rotation (in degrees) of component with respect to source

        Example of text: ROTATED (11.6, 0, 0) RELATIVE Detector_Position_t
        """
        return self._vectorRelation("ROTATED", "rotation", ROTATION, text)


    def _vectorRelation(self, property, type, regex, text):
        """
        Returns string of McVine ('position' or 'rotation')

        Output is tuple:  ((X, Y, Z), <Relation>, <Component Name>)
        Example: ((0, 0, 1.200), "relative", "arm")
        """
        prop    = self._property(property, text)
        p       = re.compile(regex, re.IGNORECASE)
        m       = p.findall(prop)

        if self._missingRotation(m, type):
            return

        # Expected format: (X, Y, Z, <Relation>, <Component>)
        if not m or not m[0] or len(m[0]) != 5:
            return (None, None, None)

        mm          = m[0]
        def _cast(v):
            try:
                return float(v)
            except:
                return v
        (x, y, z)   = map(_cast, mm[:3])

        relation    = mm[3].upper()
        if not relation in RELATION:
            raise Exception("Error: Wrong component relation")

        # ABSOLUTE relation
        if relation == "ABSOLUTE":  # Easy: just return what you have
            return ((x, y, z), "absolute", None)   #self._absoluteVector(x, y, z)
        
        # RELATIVE relation is implied
        assert relation == "RELATIVE"

        relcomp = mm[4]     # Name of relative component
        return self._relativeToComp(x, y, z, relcomp)


    def _relativeToComp(self, x, y, z, relcomp):
        """
        Returns vector coordinates relative to component relcomp

        x, y, z     -- coordinates of the current component
        relcomp     -- name of the relative component

        Output is tuple:  ((X, Y, Z), <Relation>, <Component Name>)
        """
        # Previous
        if relcomp.lower()  == "previous":
            relcomp = "previous"

        return ((x, y, z), "relative", relcomp) 


    def _rotFromPos(self, position):
        "Returns rotation from position"
        assert len(position) == 3, "Invalid position: %s" % (position,)   # 3 element tuple, Example: ((0, 0, 1.200), "relative", "arm")

        if position[1] == 'absolute':
            return (0,0,0), 'absolute'

        if not position[2]:     # Component name is None
            return ((0, 0, 0), "relative", "previous")
        
        return ((0, 0, 0), "relative", position[2])

        # Position,
        # Example 1: relative([0.0, 0.0, 0.09353], to="TRG_Out")
        # Example 2: [0.0, 0.0, 1.02]
#        p       = re.compile(RELTO, re.IGNORECASE)
#        m       = p.findall(position)
#        if not m or len(m) == 0:   # Not relative or something else
#            return self._relativeVector(0, 0, 0, "previous")    #"relative((0, 0, 0), to=\"previous\")"
#        relcomp = m[0]
#        return self._relativeVector(0, 0, 0, relcomp)   #"relative((0, 0, 0), to=\"%s\")" % relcomp


    def _missingRotation(self, match, type):
        "Returns True if rotation is missing"
        if (not match or not match[0]) and type == "rotation":
            return True

        return False


    def _removeComments(self, text):
        "Removes comments from the text"
        p   = re.compile(COMMENT, re.DOTALL)
        s   = re.sub(p, '', text)
        return s


# version
__id__ = "$Id$"

# End of file 

