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
                  This is a convenient form to create other data structures
                  and scripts (e.g. McVine components).

.toInstrString() generates script for instrument creation

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
    - Check if name is case sensitive (like COMPONENT)
    - Extract properties from "extra" to separate properties
    - Assumption is made that new line is "\n"

Questions:
    - Should I consider component type as McStas or VNF dom names?
"""

# XXX: Fix rotation part in geometer parameter in toMcvineString() (it is not generated correctly)
# XXX: Fix options issue (see fixtures.textOptions)
# XXX: Implement nice align of dictionary entries in toBuilderString()
# XXX: Implement filter for parameters and components
# XXX: Filter is not set correctly (because it does not propagate to methods that use the filter)

# XXX: Fix 
#    _formatVector() in _clParams()
#    _toString()
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
from compmodules import IMPORT_DICT, PARAMS_DICT, INSTRUMENT, PARAM_FILTER, COMP_FILTER, BUILD_DICT

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
ROTATION        = "ROTATED%s%s%s(RELATIVE|ABSOLUTE)%s([^ ]*)" % (SPACES, VECTOR, SPACES, SPACES)
RELTO           = "to=\"([^\"]+)\"" # Relative to component

# Constants
PROPERTIES      = ["AT", "ROTATED"]     # Standard properties
RELATION        = ["RELATIVE", "ABSOLUTE"]
TERMINATORS     = ["FINALLY", "END"]
FILE            = ["--filename", "-f"]
CONFIG          = ["--config", "-c"]
ARGS            = FILE + CONFIG

# McStas components base directory
COMP_BASE       = "../../../packages/legacycomponents/mcstas2/share/McStas-Components"

# Directories where the McStas components may reside
COMP_CATEGORY   = ["monitors", "optics", "samples", "sources"]

# Usage string
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
        self._components    = []    # Keeps list of dictionaries for each component

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
            self._components.append(comp)

            comp["name"]        = m[0]
            comp["type"]        = m[1]
            comp["parameters"]  = self._params(m[2])
            comp["mcstas_position"] = self._mcstasPosition(m[3])    # Position in McStas notations
            comp["mcstas_rotation"] = self._mcstasRotation(m[3])    # Rotation in McStas notations
            comp["position"]    = self._position(m[3], comp["name"], order)
            comp["rotation"]    = self._rotation(m[3], comp["name"], order)
            comp["extra"]       = self._extra(m[3])

            order   += 1


    def components(self, filter=COMP_FILTER):
        """
        Returns list of components with optional filter applied
        
        filter -- list of component types to filter out
        """
        if not filter:  # No filter applied - return all of the components
            return self._components

        complist   = []
        for c in self._components:
            if c and not (c["type"] in filter["type"] or
                          c["name"] in filter["name"]):
                complist.append(c)

        return complist


    def component(self, name):
        "Returns tuple (component, order) of first component specified by name"
        for i in range(len(self._components)):
            c   = self._components[i]
            if c["name"] == name:
                return (c, i)

        return None


    def firstComponent(self, filter=COMP_FILTER):
        "Returns first component of instrument after filtering"
        comps    = self.components(filter)
        if len(comps) == 0:
            return None
        return comps[0]


    def header(self, br="\n"):
        "Returns header for McStasConverter"
        return "# Generated by McStasConverter, %s%s%s" % (strftime("%d %b %Y %H:%M", localtime()), br, br)


    # XXX: Merge component parameters both from instrument values and component default values
    def toString(self, ind=16, br="\n", allparams=True):
        "Dumps component metadata and parameters in a pretty form"
        str     = self.header(br)

        def dottedline(br):
            return "%s%s" % ("-"*50, br)

        # List of components
        str     += "List of components: <type>: <name>%s%s%s" % (br, dottedline(br), br)
        for comp in self.components():
            str += "%s:%s%s%s" % (comp["type"], self._resIndent(comp["type"], ind), comp["name"], br)

        str     += br
        str     += br

        # Dump components
        str     += "Components details: %s%s%s" % (br, dottedline(br), br)
        for comp in self.components():
            str += "name:%s%s%s"     % (self._resIndent("name:", ind), comp["name"], br)
            str += "type:%s%s%s"     % (self._resIndent("type:", ind), comp["type"], br)
            str += "position:%s%s%s" % (self._resIndent("position:", ind),
                                        self._formatVecMcstas(comp["mcstas_position"]), br)
            str += "rotation:%s%s%s" % (self._resIndent("rotation:", ind),
                                        self._formatVecMcstas(comp["mcstas_rotation"]), br)
            str += "extra:%s%s%s"    % (self._resIndent("extra:", ind),
                                        comp["extra"], br)

            params  = comp["parameters"]
            str     += self._firstParam(params, ind, br)
            keys    = params.keys()
            if len(keys) <= 1:      # One parameter exist only
                str += br
                continue

            for key in keys[1:]:    # More than one parameter exists
                strInd  = self._resIndent("", ind)
                str     += "%s%s:%s%s%s" % (strInd, key, self._resIndent(key, ind), params[key], br)

            str += br

        return str


    # XXX: Merge component parameters both from instrument values and component default values
    def toInstrString(self, br="\n", allparams=True):
        """Returns script string for instrument generation

        Note:
            - Generated string for instrument might not be self consistent in the sense
                that some of the parameters might not be set. Please edit manually
                the generated string, if needed.
        Example of the file format: 
            ./vnfb/vnfb/dom/neutron_experiment_simulations/instruments/ARCS_beam.py
        """
        str     = self.header(br)
        
        # Generate imports
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
        str     += "from _utils import ccomp, cinstr\n"
        str     += self._instrCreate()
        return str


    # XXX: Merge component parameters both from instrument values and component default values
    def toBuilderString(self, ind=4, br="\n", allparams=True):
        """
        Returns string that generates methods in class Builder that creates
        command line parameters for job builder

        ind:    (int) -- Python indent
        br:     (str) -- new line character

        Note:
            - See: ./vnfb/vnfb/components/job_builders/neutronexperiment/InstrumentSimulationAppBuilder.py
            - This class is not complete! Generates methods for convenience purposes!
        """
        str     = self.header(br)
        str     += br
        str     += "from _ import JobBuilder as base" + br
        str     += "class Builder(base):" + br
        str     += br

        types   = self.comptypes()

        for type in types:  # Example of type: L_monitor
            str += self._onComp(type, ind, br)

        return str


    # XXX: Merge component parameters both from instrument values and component default values
    def toMcvineString(self, executable="mcvine-simulate", br="\n", allparams=True):
        "Returns *partial* command line string that is executed by McVine"
        str     = "#!/usr/bin/env bash" + br
        str     += br
        str     += self.header(br)
        str     += br
        str     += "%s \%s" % (executable, br)
        compseq  = "\t--components="
        for comp in self.components():
            compseq += "%s," % comp["name"]

        compseq = compseq.rstrip(",")     # Remove trailing comma
        str     += "%s --- \%s" % (compseq, br)

        # Add neutron counts
        str     += "\t--ncount=1000000 \%s" % br
        str     += "\t--buffer_size=100000 \%s" % br

        # Add component types
        for comp in self.components():
            str     += "\t--%s=%s \%s" % (comp["name"], comp["type"], br)
        
        # Add component parameters
        str     += self._clParams(br, allparams)

        return str


    def toVnfString(self, executable=". ~/.mcvine && python simapp.py", br="\n", allparams=True):
        """
        Returns command line string that is executed by VNF job builder

        Note:
            - simapp.py is normally created by VNF
        """
        sequence    = []
        str     = "#!/usr/bin/env bash" + br
        str     += br
        str     += "%s \%s" % (executable, br)
        str     += self._clParams(br, allparams)
        for comp in self.components():
            sequence.append(comp["name"])

        # Generate sequence
        ss  = "\t--sequence=\"["
        for s in sequence:
            ss  += "'%s', " % s

        ss  = ss.rstrip(", ")   # Remove trailing comma on the right side
        ss  += "]\""

        str     += ss + " \\" + br

        return str


    def toPmlString(self):
        return "Not Implemented"


    def _clParams(self, br="\n", allparams=True):
        "Returns command line formatted parameters"
        str = ""
        for comp in self.components():
            params  = self._compParams(comp, allparams=allparams)
            # Generate parameters
            for k, v in params.iteritems():
                # Take from the rest of the default parameters from components itself!
                str += "\t--%s.%s=%s \%s" % (comp["name"], k, self._paramValue(v), br)
            # Generate geometer
            str     += "\t--geometer.%s='%s,%s' \%s" % (    comp["name"],
                                                            self._formatVecRel(comp["position"]),
                                                            self._formatVecRel(comp["rotation"]),
                                                            br)
        return str


    def _paramValue(self, value):
        "Replaces constants in parameters by values"
        instr   = INSTRUMENT["VULCAN"]  # XXX: Specific for Vulcan
        if value in instr.keys():
            return self._quote(str(instr[value]))

        return self._quote(value)


    def _quote(self, s):
        "Takes string and makes sure that it surrounded by quota"
        if not s:
            return "\"\""

        return "'%s'" % s.strip("'").strip("\"")
        #return "\"%s\"" % s.strip("\"")


    def _compParams(self, comp, filter=PARAM_FILTER, allparams=True):
        """
        Returns dictionary of component parameters. It can accept parameters filter
        Example Output: {'xmin': '-0.025', 'ymin': '-0.045'}
        """
        params  = comp["parameters"]
        # Return those parameters that are set in an intrument only!
        if not allparams:       # Do I still need this option?
            return params

        # Add default values for parameters that are not set in instrument
        totalparams  = self._mcstasParams(comp["type"])
        for p in totalparams:               
            if not p["name"] in params.keys():  
                params[p["name"]] = p["value"]

        filteredParams = []
        if comp["type"] in filter.keys():
            filteredParams  = filter[comp["type"]]

        for pn in params.keys():
            if params[pn] == "" or (pn in filteredParams):    # Empty or filtered
                del params[pn]      # Remove parameter

        return params


    def comptypes(self):
        "Returns list of component types"
        comps   = self.components()
        ct      = []
        for c in comps:
            if not c["type"] in ct:
                ct.append(c["type"])

        return ct


    def _onComp(self, type, ind, br):
        "Returns string with component information for job builder"
        str     = br
        str     += self._ind(ind) + "def on%s(self, component):" % self._domModule(type) + br
        str     += self._ind(2*ind) + "kwds = {" + br
        str     += self._ind(3*ind) + "'name': component.componentname," + br
        str     += self._ind(3*ind) + "'category': '%s'," % self._compCategory(type) + br
        str     += self._ind(3*ind) + "'type': '%s'," % type + br
        str     += self._ind(3*ind) + "'supplier': 'mcstas2'," + br
        str     += self._ind(3*ind) + "}" + br
        str     += self._ind(2*ind) + "self.onNeutronComponent( **kwds )" + br
        str     += br
        str     += self._ind(2*ind) + "opts = {}" + br
        str     += br
        str     += self._ind(2*ind) + "parameters = {" + br

        # Move in a separate method?
        # Specify parameters
        params  = self._mcstasParams(type)
        names   = self._paramNames(params)
        for name in names:
            value   = "component.%s" % name
            if name in PARAMS_DICT.keys():
                value   = PARAMS_DICT[name]
            str     += self._ind(3*ind) + "'%s': %s," % (name, value) + br

        str     += self._ind(3*ind) + "}" + br
        str     += self._ind(2*ind) + "for k,v in parameters.iteritems():" + br
        str     += self._ind(3*ind) + "opts['%s.%s' % (component.componentname, k)] = v" + br
        str     += br
        str     += self._ind(2*ind) + "self.cmdline_opts.update( opts )" + br
        str     += br

        return str


    def _compFile(self, type, ext="comp"):
        "Returns filename of component of type"
        # Example: L_monitor.comp
        return "%s.%s" % (type, ext)


    def _compCategory(self, type):
        """
        Returns category name where the component 'type' is located
        
        Note:
            - It is implied that component of type exists in one of the category
                directories only
        """
        for cc in COMP_CATEGORY:
            path    = os.path.join(COMP_BASE, cc, self._compFile(type))
            if os.path.exists(path):
                return cc

        return ""   # Component is not in any of the COMP_CATEGORY


    def _compPath(self, type):
        """
        Finds component in the component base directory and returns relative to
        this script path to the McStas component of type
        
        Example: "../../../packages/legacycomponents/mcstas2/share/McStas-Components/monitors/L_monitor.comp"
        """
        return os.path.join(COMP_BASE, self._compCategory(type), self._compFile(type))


    def _mcstasParams(self, type):
        """
        Returns list of parameters for McStas component
        
        This includes "DEFINITION PARAMETERS" and "SETTING PARAMETERS"
        Example: [{'type': '', 'name': 'xmin', 'value': '0'}, {'type': '', 'name': 'xmax', 'value': '0'}]
        """
        filename    = self._compPath(type)
        parser      = McStasComponentParser(filename=filename)
        defs        = parser.definitions()
        setparams   = defs.get("setting_parameters")
        defparams   = defs.get("definition_parameters")
        params      = []
        paramlist   = []
        # Can be empty list but not None!
        if (setparams != None) and (defparams != None):
            paramlist   = setparams + defparams

        # Not sure if I need this?
        for p in paramlist:     
            if not self._inParams(p, params):
                params.append(p)

        return params


    def _inParams(self, p, params):
        "Checks if p dictionary in params. Used to avoid repeating parameters"
        for i in range(len(params)):
            if p["name"] == params[i]["name"]:  # Names match
                return True

        return False


    def _paramNames(self, params):
        """
        Takes param dictionaries and return param names

        Example Input: [{'type': '', 'name': 'xmin', 'value': '0'}, {'type': '', 'name': 'xmax', 'value': '0'}]
        Example Output: ['xmin', 'xmax']
        """
        return [p["name"] for p in params]
    

    def _ind(self, ind):
        "Returns ind number of spaces"
        return ind*" "


    def _domModule(self, comptype):
        "Takes component type and returns VNF dom module"
        # McStas component -> VNF dom module
        # Example: L_Monitor -> LMonitor
        if comptype in IMPORT_DICT.keys():
            return IMPORT_DICT[comptype]

        return comptype     # Names coinside


    def _instrImports(self):
        "Returns string of imports"
        ct      = self.comptypes()
        base    = "vnfb.dom.neutron_experiment_simulations.neutron_components"
        str     = "\n"
        for type in ct:
            module  = self._domModule(type)
            str += "from %s.%s import %s\n" % (base, module, module)

        str     += "\n"
        return str

        
    def _instrCompFunc(self, comp):
        "Returns string of generated instrument component"
        str     = "\n"
        if not comp:
            return str

        # Find module
        comptype    = self._domModule(comp["type"])

        str     = "def %s():\n" % comp["name"]
        str     += "    c = %s()\n" % comptype
        str     += "    c.short_description = \"%s\"\n" % comp["name"]
        params  = comp["parameters"]

        for k, v in params.iteritems():
            # Replace for example xmin -> x_min, xwidth -> x_width
            if k in BUILD_DICT.keys():
                k   = BUILD_DICT[k]
            str     += "    c.%s = %s\n" % (k, v)
        # If component is relative, set referencename
        
            
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


    def _instrComp(self, ind=" "*8):
        "Returns string of components"
        str     = "\n"
        str     += "    components = [\n"
        comps   = self.components()
        for comp in comps:
            str     += "%sccomp(\"%s\", %s(), (%s, %s, '')),\n" % (ind,
                        comp["name"],
                        comp["name"],
                        self._formatVecInstr(comp["position"]),
                        self._formatVecInstr(comp["rotation"]))

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


    def _compNames(self, filter=COMP_FILTER):
        "Returns list of component names in self._components!"
        names   = []
        for c in self.components(filter):
            names.append(c["name"])
            
        return names


    def _relComp(self, order, name):
        """
        Returns tuple (component, order) of relative component specified by name
        starting from order-1 to the source
        
        """
        for i in range(order-1, -1, -1):
            comp    = self._components[i]
            if comp["name"] == name:
                return (comp, i)

        return None     # Not found


    def _formatVecRel(self, vecrel, bracket="round"):
        """
        Formats the vector to string

        vector -- tuple of three elements: ((X, Y, Z), <Relation>, <Component Name>)
        bracket = ("round"|"square")
        """
        assert len(vecrel) == 3

        vector  = vecrel[0]
        relation    = vecrel[1]
        comp        = vecrel[2]

        if vector == None:
            return "None"

        assert len(vector) == 3
        start   = "("
        end     = ")"        
        if bracket == "square":
            start   = "["
            end     = "]"

        vecstr      = "%s%.5f, %.5f, %.5f%s" % (start, vector[0], vector[1], vector[2], end)

        if relation != "relative":  # Not relative: None or "absolute"
            return vecstr

        if comp == None:    # No component specified
            comp    = "previous"

        return "relative(%s, to=\"%s\")" % (vecstr, comp)


    def _formatVecMcstas(self, mcstasvec):
        "Formats McStas vector. No actual formatting performed"
        return mcstasvec


    def _formatVecInstr(self, vecrel, bracket="round"):
        return ""


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
            relcomp = self._relComp(order, name)
            comp    = relcomp[0]
        else:
            comp    = self._components[order-1]

        return comp[type]
        

    def _position(self, text, compname, order):
        """
        Returns absolute position of component with respect to source

        Example of text: AT (0, 0, 0.39855)  RELATIVE  PREVIOUS

        compname    -- component name to which rotation is applied
        """
        return self._vectorRelation("AT", "position", POSITION, compname, order, text)
        

    def _rotation(self, text, compname, order):
        """
        Returns absolute rotation (in degrees) of component with respect to source

        Example of text: ROTATED (11.6, 0, 0) RELATIVE Detector_Position_t

        compname    -- component name to which rotation is applied
        """
        return self._vectorRelation("ROTATED", "rotation", ROTATION, compname, order, text)


    def _mcstasPosition(self, text):
        """
        Returns position string in McStas notations
        """
        return self._property("AT", text)


    def _mcstasRotation(self, text):
        """
        Returns rotation string in McStas notations
        """
        return self._property("ROTATED", text)


    def _vectorRelation(self, property, type, regex, compname, order, text):
        """
        Returns string of McVine ('position' or 'rotation')

        Output is tuple:  ((X, Y, Z), <Relation>, <Component Name>)
        Example: ((0, 0, 1.200), "relative", "arm")
        """
        prop    = self._property(property, text)
        p       = re.compile(regex, re.IGNORECASE)
        m       = p.findall(prop)

        if self._missingRotation(m, type):
            # Missing rotation parameter means (0, 0, 0) rotation
            return  self._rotFromPos(order)     

        # Expected format: (X, Y, Z, <Relation>, <Component>)
        if not m or not m[0] or len(m[0]) != 5:
            return (None, None, None)

        mm          = m[0]
        (x, y, z)   = (float(mm[0]), float(mm[1]), float(mm[2]))

        relation    = mm[3].upper()
        if not relation in RELATION:
            raise Exception("Error: Wrong component relation")

        # ABSOLUTE relation
        if relation == "ABSOLUTE":  # Easy: just return what you have
            return ((x, y, z), "absolute", None)   #self._absoluteVector(x, y, z)
        
        # RELATIVE relation is implied
        assert relation == "RELATIVE"

        relcomp = mm[4]     # Name of relative component
        return self._relativeToComp(x, y, z, relcomp, order)


    def _relativeToComp(self, x, y, z, relcomp, order):
        """
        Returns vector coordinates relative to component relcomp

        x, y, z     -- coordinates of the current component
        relcomp     -- name of the relative component
        order       -- order of the current component

        Output is tuple:  ((X, Y, Z), <Relation>, <Component Name>)
        """
        if self._isFirstComp(order):    # First component returns absolute position
            return ((0, 0, 0), "absolute", None)    #self._absoluteVector(0, 0, 0)

        # If relative component is of Arm type, make it relative to component before Arm
        if self._isArm(relcomp):
            if self._ifFirstArm(relcomp):
                return ((x, y, z), "absolute", None)    #self._absoluteVector(x, y, z)

            # Arms after the first arm
            tuple       = self.component(relcomp)
            armOrder    = tuple[1]
            comp        = self._prevToArm(armOrder)
            return ((x, y, z), "relative", "previous") #self._relativeVector(x, y, z, "previous")    # XXX: Temp
            #return self._relativeVector(x, y, z, comp["name"])
        
        # Previous
        if relcomp.lower()  == "previous":
            relcomp = "previous"

        return ((x, y, z), "relative", relcomp)     #self._relativeVector(x, y, z, relcomp)


    def _rotFromPos(self, order):
        "Returns rotation from position"
        # Make sure that position is already set!
        comp        = self._components[order]
        position    = comp["position"]
        assert len(position) == 3   # 3 element tuple, Example: ((0, 0, 1.200), "relative", "arm")

        if self._isFirstComp(order):    # First component returns absolute position
            return ((0, 0, 0), "absolute", None) #self._absoluteVector(0, 0, 0)

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


    def _prevToArm(self, order):
        """
        Returns  non-Arm component closest and positioned before the Arm component
        
        order   -- order of current component
        relname -- name of component to which the current component referse to
        """
        for i in range(order-1, -1, -1):
            comp    = self._components[i]
            if comp["type"] != "Arm":   
                return comp

        return None     # Not found
        


    def _firstArm(self):
        "Returns first component of type Arm"
        for c in self._components:
            if c["type"] == "Arm":
                return c

        return None


    def _ifFirstArm(self, name):
        "Returns if component specified by name is the first arm"
        firstArm    = self._firstArm()
        if firstArm["name"] == name:
            return True

        return False


    def _isArm(self, name):
        "Checks if comp of name is of Arm type"
        comp    = self.component(name)
        if comp and comp[0]["type"] == "Arm":
            return True

        return False


    def _isFirstComp(self, order):
        "Returns True if order corresponds to the first component"
        first   = self.firstComponent()
        if not first:   # No first component available
            return False
            
        name    = first["name"]
        comp    = self.component(name)

        if comp and comp[1] == order:
            return True

        return False
        

    def _absoluteVector(self, x, y, z):
        "Returns absolute vector"
        return "(%s, %s, %s)" % (x, y, z)


    def _relativeVector(self, x, y, z, relcomp):
        "Returns vector relative to relcomp"
        return "relative((%s, %s, %s), to=\"%s\")" % (x, y, z, relcomp)


    def _missingRotation(self, match, type):
        "Returns True if rotation is missing"
        if (not match or not match[0]) and type == "rotation":
            return True

        return False


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
            #print conv.toInstrString()
            #print conv.toBuilderString()
            print conv.toMcvineString()
            #print conv.toVnfString()
            #print conv.toPmlString(self)
            #print conv.component("TRG_Out")
            return

    print USAGE_MESSAGE
    return


if __name__ == "__main__":
    main()

__date__ = "$Aug 19, 2010 10:25:18 AM$"

