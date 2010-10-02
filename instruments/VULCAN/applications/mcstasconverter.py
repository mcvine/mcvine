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
McStasConverter - converter for McStas components to list of dictionaries.
                  This a convenient form to create other data structures
                  (e.g. McVine components)


Example:

McStas component:

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

Issues:
    - Check if name is case sensitive (like COMPONENT)
    - Extract properties from "extra" to separate properties
    - Assumption is made that new line is "\n"
"""

"""
XXX: Fix options issue (see fixtures.textOptions)
XXX: Fix absolute position and rotation
- Learn format position and rotation options
- Options are case non-sensitive
- "Relative <COMP>" means relative to the nearest to source component
- Position format:
    AT (x, y, z) RELATIVE <Name>
    AT (x, y, z) ABSOLUTE
    AT (x, y, z) RELATIVE PREVIOUS

- Rotation format:
    ROTATED (Ax, Ay, Az) RELATIVE name
    ROTATED (Ax, Ay, Az) ABSOLUTE
    AT (x, y, z) RELATIVE PREVIOUS ROTATED (Ax, Ay, Az) RELATIVE PREVIOUS(2) # Not supported
- 

"""

# Imports
import re
import sys
import os.path
from time import localtime, strftime

# Regular expressions
COMMENT         = '(/\*.*?\*/)'         # Non-greedy comment (.*?)
SPACES          = '[ \t]*'              # Spaces and tabs
NAME            = '%s([^ ()=]*)%s' % (SPACES, SPACES)  # Extracts name
NO_BRACKETS     = '[^()]*'              # No brackets
PARAMETERS      = '(%s)' % NO_BRACKETS  # Component parameters
COMPONENT       = "%s=%s\(%s\)(.*)" %(NAME, NAME, PARAMETERS)  # Component
VECVAL          = "([^,\)]+)"             # Vector's value
VECTOR          = "\(%s,%s,%s\)" % (VECVAL, VECVAL, VECVAL) # Vector
VECTOR_F        = "(\([^\)]*\))"
POSITION        = "AT%s%s%s(RELATIVE|ABSOLUTE)%s([^ ]*)" % (SPACES, VECTOR, SPACES, SPACES)

# Constants
PROPERTIES      = ["AT", "ROTATED"]     # Standard properties
RELATION        = ["RELATIVE", "ABSOLUTE"]
TERMINATORS     = ["FINALLY", "END"]
COMP_IGNORE     = ["Progress_bar", "Arm"]
FILE            = ["--filename", "-f"]
CONFIG          = ["--config", "-c"]
ARGS            = FILE + CONFIG
USAGE_MESSAGE   = """NAME:
    McStasConverter - converter for McStas components 

SYNOPSIS:
    python mcstasconverter.py [--filename|-f=file_name] [--config|-c=config_string]

DESCIRPTION:
    McStasConverter - class that performs convertion from McStas components to dictionary.
                      This a convenient form to create other data structures
                      (e.g. McVine components)
"""

# Utils
ifelse  = lambda a,b,c: (b,c)[not a]    # C ternary operator '?:'

class McStasConverter:

    def __init__(self, filename=None, config=None, parse=True):
        self._filename      = filename
        self._config        = config
        self._components    = []    # list of dictionaries

        if parse and (self._fileExists() or config):
            self.parse()


    def parse(self):
        "Parses file content and appends component to self._components"
        configText   = self._configText()
        
        # Remove comments
        text         = self._removeComments(configText)
        compSplits   = text.split("COMPONENT")   # Split by component parts
        compSplits   = compSplits[1:]             # Skip 0 part (should not have components)

        # Go over the component strings and populate components
        order       = 0
        for compText in compSplits:
            p   = re.compile(COMPONENT, re.DOTALL)
            # Finds all components (well, there should be one component)
            matches     = p.findall(compText)

            if not matches or not matches[0]: # No match, procede to the next candidate
                continue

            # Populate component
            m = matches[0]
            comp    = {}
            comp["name"]        = m[0]
            comp["type"]        = m[1]
            comp["parameters"]  = self._params(m[2])
            comp["position"]    = self._position(m[3], order)
            comp["rotation"]    = self._rotation(m[3], order)
            comp["extra"]       = self._extra(m[3])

            self._components.append(comp)
            order   += 1


    def components(self, filter=COMP_IGNORE):
        """
        Returns list of components
        
        filter -- list of component types to filter out
        """
        if not filter:  # No filter applied - return all of the components
            return self._components

        complist   = []
        for c in self._components:
            if c and not (c["type"] in filter):
                complist.append(c)

        return complist


    def toString(self, indent=16, br="\n"):
        "Dumps component metadata and parameters in a pretty form"
        str     = "# Generated by McStasConverter, %s%s%s" % (strftime("%d %b %Y %H:%M", localtime()), br, br)


        def dottedline(br):
            return "%s%s" % ("-"*50, br)

        # List of components
        str     += "List of components: <type>: <name>%s%s%s" % (br, dottedline(br), br)
        for comp in self.components():
            str += "%s:%s%s%s" % (comp["type"], self._resIndent(comp["type"], indent), comp["name"], br)

        str     += br
        str     += br

        # Dump components
        str     += "Components details: %s%s%s" % (br, dottedline(br), br)
        for comp in self.components():
            str += "name:%s%s%s"     % (self._resIndent("name:", indent), comp["name"], br)
            str += "type:%s%s%s"     % (self._resIndent("type:", indent), comp["type"], br)
            str += "position:%s%s%s" % (self._resIndent("position:", indent), self._formatVector(comp["position"]), br)
            str += "rotation:%s%s%s" % (self._resIndent("rotation:", indent), comp["rotation"], br) # self._formatVector(comp["rotation"])
            str += "extra:%s%s%s"    % (self._resIndent("extra:", indent), comp["extra"], br)

            params  = comp["parameters"]
            str     += self._firstParam(params, indent, br)
            keys    = params.keys()
            if len(keys) <= 1:      # One parameter exist only
                str += br
                continue

            for key in keys[1:]:    # More than one parameter exists
                strInd  = self._resIndent("", indent)
                str     += "%s%s:%s%s%s" % (strInd, key, self._resIndent(key, indent), params[key], br)

            str += br

        return str


    # XXX: Fix position and rotation for generated component!
    def toInstrString(self, br="\n"):
        """Returns script string for instrument generation

        Note:
            - Generated string for instrument might not be self consistent in the sense
              that some of the parameters might not be set. Please edit manually
              the generated string, if needed.
        Example of the file format: 
            ./vnfb/vnfb/dom/neutron_experiment_simulations/instruments/ARCS_beam.py
        """
        str     = "# Generated by McStasConverter, %s%s%s" % (strftime("%d %b %Y %H:%M", localtime()), br, br)
        
        # Generate imports
        str     += "from _utils import ccomp, cinstr\n"
        str     += self._instrImports()
        # Special import: NeutronRecorder
        str     += "from vnfb.dom.neutron_experiment_simulations.neutron_components.NeutronRecorder import NeutronRecorder\n\n"

        # Generate component functions
        for comp in self.components():
            str += self._instrCompFunc(comp)

        # Special case: "neutron_recorder"
        str     += "\n"
        str     += "def neutron_recorder():\n"
        str     += "    c = NeutronRecorder()\n"
        str     += "    c.short_description = \"Neutron recorder at sample position\"\n"
        str     += "    return c\n\n"

        # Generate instrument
        str     += self._instrCreate()
        return str


    def comptypes(self):
        "Returns list of component types"
        comps   = self.components()
        ct      = []
        for c in comps:
            if not c["type"] in ct:
                ct.append(c["type"])

        return ct


    def _instrImports(self):
        "Returns string of imports"
        ct      = self.comptypes()
        base    = "vnfb.dom.neutron_experiment_simulations.neutron_components"
        str     = "\n"
        for mod in ct:
            str += "from %s.%s import %s\n" % (base, mod, mod)

        str     += "\n"
        return str

        
    def _instrCompFunc(self, comp):
        "Returns string of generated instrument component"
        str     = "\n"
        if not comp:
            return str
        
        str     = "def %s():\n" % comp["name"]
        str     += "    c = %s()\n" % comp["type"]
        str     += "    c.short_description = \"%s\"\n" % comp["name"]
        params  = comp["parameters"]

        for k, v in params.iteritems():
            str     += "    c.%s = %s\n" % (k, v)
        str     += "    return c\n\n"
        return str


    def _instrCreate(self):
        "Returns string of 'createInstrument()' function"
        str     = "\n"
        str     += "def createInstrument(director):"
        # Generate components list
        str     += self._instrComp()

        # Generate instrument dictionary
        str     += self._instrMeta()
        return str


    # XXX: Fix absolute position and rotation
    def _instrComp(self, ind=" "*8):
        "Returns string of components"
        str     = "\n"
        str     += "    components = [\n"
        comps   = self.components()
        for comp in comps:
            str     += "%sccomp(\"%s\", %s(), (%s, %s, '')),\n" % (ind,
                        comp["name"], comp["name"], self._formatVector(comp["position"]), comp["rotation"]) # self._formatVector(comp["rotation"])

        str     += "%s]\n\n" % ind
        return str


    def _instrMeta(self, ind=" "*8):
        "Returns string of instrument metadata"
        str     = "\n"
        
        str     += "    instrument = cinstr(\n"
        str     += "%sdirector,\n" % ind
        str     += "%sname = \"\",\n" % ind
        str     += "%sshort_description = \"\",\n" % ind
        str     += "%slong_description = \"\",\n" % ind
        str     += "%scategory = \"\",\n" % ind
        str     += "%screator = \"VNF\",\n" % ind
        str     += "%sdate = \"%s\",\n" % (ind, strftime("%d %b %Y %H:%M", localtime()))
        str     += "%scomponents = components\n" % ind
        str     += "%s)\n\n" % ind
        return str


    def _fileExists(self):
        "Checks if file exists"
        if self._filename and os.path.exists(self._filename):
            return True

        return False


    def _configText(self):
        "Take config from file if it exist and readable, or use from config - otherwise"
        configText  = ""
        if self._fileExists():
            try:    # Try to read it
                configText  = open(self._filename).read()
            except:
                pass    # No exception
            return configText

        if self._config:
            configText  = self._config

        return configText   # Empty string


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


    def _removeComments(self, text):
        "Removes comments from the text"
        p   = re.compile(COMMENT, re.DOTALL)
        s   = re.sub(p, '', text)
        return s


    def _vector(self, property, type, regex, order, text):
        "Returns vector formatted or not"
        # Default vector is taken from previous component
        pos     = self._prevVector(order, type)
        prop    = self._property(property, text)
        p       = re.compile(regex, re.IGNORECASE)
        m       = p.findall(prop)
        # Expected format: (X, Y, Z, <Relation>, <Component>)
        if not m or not m[0] or len(m[0]) != 5:
            return pos

        mm          = m[0]
        (x, y, z)   = (float(mm[0]), float(mm[1]), float(mm[2]))

        relation    = mm[3].upper()
        if not relation in RELATION:
            raise Exception("Error: Wrong component relation")

        # ABSOLUTE relation
        if relation == "ABSOLUTE":  # Easy: just return what you have
            return (x, y, z)

        # RELATIVE relation is implied
        assert relation == "RELATIVE"

        relcomp = mm[4]     # Name of relative component
        if relcomp != "ABSOLUTE" and relcomp in self._compNames(filter=None):
            pos = self._prevVector(order, type, relcomp)

        return (x + pos[0], y + pos[1], z + pos[2])

#        if relcomp.upper() == "PREVIOUS":
#            pos = self._prevVector(order, "position")


#    def _vector(self, type, text, format):
#        "Returns vector formatted or not"
#        prop    = self._property(type, text)
#
#        if format:      # Return string
#            p       = re.compile(VECTOR_F)
#            m       = p.findall(prop)
#            pos     = "(0, 0, 0)"
#            if not m or not m[0]:
#                return pos
#
#            return m[0].strip()
#
#        pos     = (0, 0, 0) # default position
#        p       = re.compile(VECTOR)
#        m       = p.findall(prop)
#        if not m or not m[0] or not len(m[0]) == 3:
#            return pos
#
#        return (float(m[0][0]), float(m[0][1]), float(m[0][2])) # Return tuple


    def _compNames(self, filter=COMP_IGNORE):
        "Returns list of component names in self._components!"
        names   = []
        for c in self.components(filter):
            names.append(c["name"])
            
        return names


    def _relComp(self, order, name):
        "Returns relative component specified by name starting from order-1 to the source"
        for i in range(order-1, -1, -1):
            comp    = self._components[i]
            if comp["name"] == name:
                return comp

        return None     # Not found


    def _formatVector(self, vector):
        "Formats the vector to string"
        assert len(vector) == 3
        return "(%.5f, %.5f, %.5f)" % vector


    def _prevVector(self, order, type, name=None):
        """
        Returns vector (position or rotation) of the previous component,
            OR of the component specified by name if it is set

        Note:
            - "type" can be either "position" or "rotation"
            - Vector of the first component is set to (0, 0, 0)
        """
        # Set position of the previous component
        if len(self._components) < 2:
            return (0.0, 0.0, 0.0) # Default vector

        # General case
        assert order > 0
        if name:
            comp    = self._relComp(order, name)
        else:
            comp    = self._components[order-1]

        return comp[type]
        

    def _position(self, text, order):
        """
        Returns absolute position of component with respect to source

        Notes:
            - Position order is specified from non-filtered components
            - Example of text: AT (0, 0, 0.39855)  RELATIVE  PREVIOUS
            - Position is a required parameter
            - Rotation is optional
            - When rotation (or position) is not specified, take value from the previous one
              or (0, 0, 0) as default
        """
        return self._vector("AT", "position", POSITION, order, text)

#        # Default vector is taken from previous component
#        pos     = self._prevVector(order, "position")
#        prop    = self._property("AT", text)
#        p       = re.compile(POSITION, re.IGNORECASE)
#        m       = p.findall(prop)
#        # Expected format: (X, Y, Z, <Relation>, <Component>)
#        if not m or not m[0] or len(m[0]) != 5:
#            return pos
#
#        mm          = m[0]
#        (x, y, z)   = (float(mm[0]), float(mm[1]), float(mm[2]))
#
#        relation    = mm[3].upper()
#        if not relation in RELATION:
#            raise Exception("Error: Wrong component relation")
#
#        # ABSOLUTE relation
#        if relation == "ABSOLUTE":  # Easy: just return what you have
#            return (x, y, z)
#
#        # RELATIVE relation is implied
#        assert relation == "RELATIVE"
#
#        relcomp = mm[4]     # Name of relative component
##        if relcomp.upper() == "PREVIOUS":
##            pos = self._prevVector(order, "position")
#
#        if relcomp != "ABSOLUTE" and relcomp in self._compNames(filter=None):
#            pos = self._prevVector(order, "position", relcomp)
#
#        return (x + pos[0], y + pos[1], z + pos[2])
        

    def _rotation(self, text, order):
        "Extracts rotation from text"
        # Example of text: ROTATED (11.6, 0, 0) RELATIVE Detector_Position_t
        #return self._vector("ROTATED", text, True)
        return "(0, 0, 0)"

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


    def _resIndent(self, str, indent):
        "Returns residual indent string"
        num = len(str)
        res = indent - num

        if res > 0:
            return res*" "

        return " "


    def _firstParam(self, params, indent, br="\n"):
        "Returns first line with parameters"
        str     = "parameters:"
        keys    = params.keys()
        if not keys:    # No parameters
            str += br
            return str

        key     = keys[0]
        str     += "%s%s:%s%s%s" % ( self._resIndent("parameters:", indent),
                                    key,
                                    self._resIndent(key, indent),
                                    params[key],
                                    br)
        return str


def main():
    for arg in sys.argv:
        parts   = arg.split("=")
        key     = parts[0]
        if key in ARGS:
            if parts[0] in FILE:
                conv    = McStasConverter(filename=parts[1])
            elif parts[0] in CONFIG:
                conv    = McStasConverter(config=parts[1])
                
            #print conv.toString()
            print conv.toInstrString()
            #print conv.components(filter=None):
            return

    print USAGE_MESSAGE
    return


if __name__ == "__main__":
    main()

__date__ = "$Aug 19, 2010 10:25:18 AM$"



#"relative" - relative vector (x, y, z)
#        # Set position of the previous component
#        if len(self._components) > 0:
#            assert order > 0
#            comp    = self._components[order-1]
#            pos     = comp["position"]
#        else:
#            pos     = (0.0, 0.0, 0.0)

        #comp    = None
#            assert order > 0   # positive order
#            comp    = self._components[order-1]
            
            #comp    = self._relComp(order, relcomp)

#        if comp:    # Relative component, if found
#            pos     = comp["position"]  # Position of the previous component
#            return (x + pos[0], y + pos[1], z + pos[2])

        # Default relation (if everything breaks)
#        return (x, y, z)

        # DEFAULT
        #return self._vector("AT", text, format)

