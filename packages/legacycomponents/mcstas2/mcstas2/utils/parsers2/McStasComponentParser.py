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
McStasComponentParser - parser for McStas components

Flexibility:
    - Stars in the header might not need to start from the very beginning
      starting spaces allowed: '*' and ' *' have the same effect
    - Sections can be in arbitrary order.


Restrictions:
    - First comment is considered to be a header!
    - Descriptions (short and full) CANNOT have ':' character!
    - Header must be finished by '%E' directive
    - Example parameter should be in Description section
    - Input subsection should go before output subsection
    - Input and output subsections should have parameters only!
    - Input and output parameters are separated from the corresponding
      decsription by semicolumn with format: <name>:{spaces}<description>
        Example: "xmin:     Lower x bound of detector opening (m)"
    - Values (description) of input and output parameters can have new line ('\n')
        but should not have ':' character


Algorithm steps:
    - Extract header (first /*...*/ comment)
    - Remove stars and spaces after them ('{spaces}*{spaces}' -> '')
    - Remove '\r' for Windows files
    - Find first occurence of pattern: "Component: ...\n" and cut the part above it
      and replace by empty string ""
    - Split by lines and go over them to populate header dict
    - Find first occurence of pattern: "Example: ...{no DIRECTIVES}" and cut the part above it
      and replace by empty string ""


Notes:
    - McStas component format: http://neutron.risoe.dk/documentation/mcdoc/
    - Names for header and input/output parameters are kept for backward compatibility


TODO:
    - Improve _populateParams() to be used in _parseInfoSection()
"""

# Imports
import re
import sys
import os.path
from time import localtime, strftime

# Utils (?)
def paramRegex(name):
    "Returns parameter regex specified by name"
    return "^(%s):([^\n]*)" % name

# Constants
INFO            = "%I"
DESCRIPTION     = "%D"
PARAMS          = "%P"
END             = "%E"
SECTIONS        = [INFO, DESCRIPTION, PARAMS] # Standard order
DIRECTIVES      = SECTIONS + [END,]
COPYRIGHT_N     = "Written by"
DATE_N          = "Date"
VERSION_N       = "Version"
ORIGIN_N        = "Origin"
RELEASE_N       = "Release"

# Allowed info parameters
STD_PARAMS      = [DATE_N, VERSION_N, ORIGIN_N, RELEASE_N]
INFO_PARAMS     = STD_PARAMS + [COPYRIGHT_N,]

FILE            = ["--filename", "-f"]
CONFIG          = ["--config", "-c"]
ARGS            = FILE + CONFIG
USAGE_MESSAGE   = """NAME:
    McStasComponentParser - parser for McStas components

SYNOPSIS:
    python McStasComponentParser.py [--filename|-f=file_name] [--config|-c=config_string]

DESCIRPTION:
    McStasComponentParser - class that performs parsing of McStas components.
"""

# Regular expressions
COMMENT         = '(/\*.*?\*/)'             # Non-greedy comment (.*?)
SPACES          = '[ \t]*'                  # Spaces and tabs
WINCR           = '\r'                      # Window's CR
STAR            = "^%s[\*]*%s" % (SPACES, SPACES)   # Starting stars
PARAM           = "^([^\:]*?):([^\n]*)"     # Parameter
IOPARAM         = "^([^\:]*?):([^\:]*)"     # Input/Output parameters
COMP_NAME       = "Component:([^\n]*)\n\n"  # Component name
EXAMPLE         = "Example:(.*?)\n\n"       # Example

INFO_SEC        = "%s(.*?)(?=%s|%s|%s)" % (INFO, DESCRIPTION, PARAMS, END)  # Info section
DESC_SEC        = "%s(.*?)(?=%s|%s|%s)" % (DESCRIPTION, INFO, PARAMS, END)  # Description section
PARAM_SEC       = "%s(.*?)(?=%s|%s|%s)" % (PARAMS, INFO, DESCRIPTION, END)  # Parameters section

INPUT_PARAMS    = "INPUT PARAMETERS:(.*)"   # Should exist?
OUTPUT_PARAMS   = "OUTPUT PARAMETERS:(.*)"  # Might not be exist


class McStasComponentParser(object):

    def __init__(self, filename=None, config=None, parse=True):
        self._filename      = filename
        self._config        = config
        # OrderedDict?
        self._header        = {}
        self._inputparams   = {}
        self._outputparams  = {}

        if parse and (self._fileExists() or config):
            self.parse()        


    def parse(self):
        """
        Parses data from config string or file and populates header structure
        """
        configText   = self._configText()

        p           = re.compile(COMMENT, re.DOTALL)
        matches     = p.findall(configText)
        if len(matches) < 1: # No header
            return

        text        = matches[0]                # First comment is the header
        text        = self._strip(WINCR, text)     # Strip carriage return
        headertext  = self._strip(STAR, text)   # Strip stars

        # Extract sections from headertext (hide them?)
        info        = self._sectionText(INFO_SEC, headertext)
        desc        = self._sectionText(DESC_SEC, headertext)
        param       = self._sectionText(PARAM_SEC, headertext)

        self._parseCompName(headertext)
        self._parseInfoSection(info)
        self._parseDescSection(desc)
        self._parseParamSection(param)


    def header(self):
        "Returns header"
        return self._header


    def inputparams(self):
        "Returns input parameters"
        return self._inputparams

        
    def outputparams(self):
        "Returns output parameters"
        return self._outputparams


    def toString(self, br="\n"):
        str     = ""
        for (key, value) in self._header.iteritems():
            str += "%s: %s%s" % (key, value, br)

        return str


    def _configText(self):
        "Take config from file if it exist and readable, or use from config - otherwise"
        configText  = ""
        if self._fileExists():
            try:        # Try to read it
                configText  = open(self._filename).read()
            except:
                pass    # No exception
            return configText

        if self._config:
            configText  = self._config

        return configText   # Empty string


    def _fileExists(self):
        "Checks if file exists"
        if self._filename and os.path.exists(self._filename):
            return True

        return False


    def _strip(self, regex, text):
        "Strips piece of text that matches regex pattern"
        p   = re.compile(regex, re.DOTALL|re.MULTILINE)
        s   = re.sub(p, '', text)
        return s


    def _parseCompName(self, text):
        p           = re.compile(COMP_NAME, re.IGNORECASE)
        namefinds   = p.findall(text)
        if not namefinds:
            return ""    # Empty name
        
        compname    = namefinds[0].strip()
        self._header["componentname"]    = compname        


    def _sectionText(self, secregex, text):
        "Returns section string that matches secregex pattern"
        p           = re.compile(secregex, re.DOTALL)
        matches     = p.findall(text)
        if len(matches) < 1: # No section found, return empty string
            return ""
        
        return matches[0]   # Return the first found match


    # XXX: Merge with _populateParams()
    def _parseInfoSection(self, text):
        "Parses info section and populates part of header parameters"
        # XXX: There might be problems that description has ':' character
        #           In this case check if numbr == 2 and afterparam = True
        lines       = text.split("\n")

        for l in lines:
            l   = l.strip()
            if l == '':
                continue    # Skip empty line

            p   = re.compile(PARAM)
            m   = p.match(l)
            
            if m:
                param       = m.group(1).strip()
                value       = m.group(2).strip()
                paramname   = self._paramName(param)
                if not paramname:
                    continue
                    
                paramname   = paramname.lower()
                self._header[paramname] = value
            else:
                self._header["simple_description"]    = l                
            

    def _paramName(self, param):
        """
        Returns parameter name.
        Note: Only those parameter which are in INFO_PARAMS will be returned
        """
        # Non standard parameter
        if self._isMatch(COPYRIGHT_N, param):
            return "copyright"

        # Standard parameters
        for regex in STD_PARAMS:
            if self._isMatch(regex, param):
                return param

        return None


    def _isMatch(self, regex, text):
        "Returns True if matches, False - otherwise"
        p       = re.compile(regex, re.IGNORECASE)
        m       = p.match(text)
        if m:
            return True # There is the match

        return False


    def _parseDescSection(self, text):
        "Parses description section and populates part of header parameters"
        # Find example
        p           = re.compile(EXAMPLE, re.DOTALL|re.IGNORECASE)
        matches     = p.findall(text)
        example     = ""        # Default value
        if len(matches) >= 1:   # No section found, return empty string
            mstr = matches[0]   # Take first match!
            if mstr:
                example  = " ".join(mstr.strip(" \n").split("\n"))

        self._header["example"]    = example

        # Get full description: strip example and take whatever is left
        text        = self._strip(EXAMPLE, text)
        self._header["full_description"]    = text.strip()


    def _parseParamSection(self, text):
        "Parses parameter section and populates input and output parameters of header"
        # Get output parameters first!
        outputtext      = self._sectionText(OUTPUT_PARAMS, text)
        filteredtext    = self._strip(OUTPUT_PARAMS, text)

        # ... and then input parameters
        inputtext       = self._sectionText(INPUT_PARAMS, filteredtext)

        self._parseInputSubsection(inputtext)
        self._parseOutputSubsection(outputtext)


    def _parseInputSubsection(self, text):
        "Parses input text and populates input parameters"
        self._inputparams  = self._populateParams(IOPARAM, text)
        self._header["input_parameters"]    = self._inputparams


    def _parseOutputSubsection(self, text):
        "Parses output text and populates output parameters"
        self._outputparams  = self._populateParams(IOPARAM, text)
        self._header["output_parameters"]   = self._outputparams


    def _populateParams(self, paramregex, text):
        "Populates dictionary of parameters"
        params      = {}
        lines       = text.split("\n")

        for l in lines:
            l   = l.strip()
            if l == '':
                continue    # Skip empty line

            p   = re.compile(paramregex)
            m   = p.match(l)

            if m:
                (param, value)  = (m.group(1).strip(), m.group(2).strip())
                # XXX: What if value has '\n'?
                if not param:
                    continue
                    
                params[param]   = value

        return params


def main():
    for arg in sys.argv:
        parts   = arg.split("=")
        key     = parts[0]
        if key in ARGS:
            if parts[0] in FILE:
                conv    = McStasComponentParser(filename=parts[1])
            elif parts[0] in CONFIG:
                conv    = McStasComponentParser(config=parts[1])

            print conv.toString()
            return

    print USAGE_MESSAGE
    return


if __name__ == "__main__":
    main()


__date__ = "$Sep 15, 2010 3:05:52 PM$"


