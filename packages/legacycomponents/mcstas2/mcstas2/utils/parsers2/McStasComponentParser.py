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

# McStas component format: http://neutron.risoe.dk/documentation/mcdoc/

"""
McStasComponentParser - parser for McStas components

Declarations:
    - First comment is considered to be a header!
    - Stars in the header might not need to start from the very beginning
      starting spaces allowed: '*' and ' *' have the same effect
    - Input and output parameters are separated from the corresponding
      decsription by semicolumn with format: <name>:{spaces}<description>
        Example: "xmin:     Lower x bound of detector opening (m)"
    -

Notes:
    -
"""

import re

# Constants
INFO        = "%I"
DESCRIPTION = "%D"
PARAMS      = "%P"
END         = "%E"
SECTIONS    = [INFO, DESCRIPTION, PARAMS]
DIRECTIVES  = SECTIONS + [END,]

# Regular expressions
COMMENT         = '(/\*.*?\*/)'         # Non-greedy comment (.*?)
SPACES          = '[ \t]*'              # Spaces and tabs
WINCR           = '\r'                  # Window's CR
STAR            = "%s\*%s" % (SPACES, SPACES)   # Starting star


class McStasComponentParser:

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
        Parses config string or file and appends component to self._components

        Algorithm steps:
        - Extract header (first /*...*/ comment)
        - Remove stars and spaces after them ('*{spaces}' -> '')
        - Remove '\r' for Windows files
        - Find first occurence of pattern: "Component: ...\n" and cut the part above it
          and replace by empty string ""
        - Split by lines and go over them to populate header dict
        - Find first occurence of pattern: "Example: ...{no DIRECTIVES}" and cut the part above it
          and replace by empty string ""
        """

        configText   = self._configText()

        p           = re.compile(COMMENT, re.DOTALL)
        matches     = p.findall(configText)
        if len(matches) < 1: # No header
            return

        m           = matches[0]    # First comment is the header
        text        = self._strip(WINCR, m)
        text        = self._strip(STAR, text)
        print text

        # Names are kept for backward compatibility
        self._header["componentname"]    = ""
        self._header["copyright"]    = ""
        self._header["simple_description"]    = ""
        self._header["full_description"]    = ""
        self._header["example"]     = ""
        self._header["input_parameters"]    = self._inputparams
        self._header["output_parameters"]    = self._outputparams



    def header(self):
        return self._header


    def toString(self, br="\n"):
        return ""


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


    def _fileExists(self):
        "Checks if file exists"
        if self._filename and os.path.exists(self._filename):
            return True

        return False


    def _strip(self, regex, text):
        "Strips piece of text that matches regex pattern"
        p   = re.compile(regex, re.DOTALL)
        s   = re.sub(p, '', text)
        return s

testtext = """
/*******************************************************************************
*
*
*
* McStas, neutron ray-tracing package
*         Copyright 1997-2002, All rights reserved
*         Risoe National Laboratory, Roskilde, Denmark
*         Institut Laue Langevin, Grenoble, France
*
* Component: E_monitor
*
* %I
* Written by: Kristian Nielsen and Kim Lefmann
* Date: April 20, 1998
* Version: $Revision: 438 $
* Origin: Risoe
* Release: McStas 1.6
*
* Energy-sensitive monitor.
*
* %D
* A square single monitor that measures the energy of the incoming neutrons.
*
* Example: E_monitor(xmin=-0.1, xmax=0.1, ymin=-0.1, ymax=0.1,
*                 Emin=1, Emax=50, nchan=20, filename="Output.nrj")
*
* %P
* INPUT PARAMETERS:
*
* xmin:     Lower x bound of detector opening (m)
* xmax:     Upper x bound of detector opening (m)
* ymin:     Lower y bound of detector opening (m)
* ymax:     Upper y bound of detector opening (m)
* Emin:     Minimum energy to detect (meV)
* Emax:     Maximum energy to detect (meV)
* nchan:    Number of energy channels (1)
* filename: Name of file in which to store the detector image (text)
*
* OUTPUT PARAMETERS:
*
* E_N:      Array of neutron counts
* E_p:      Array of neutron weight counts
* E_p2:     Array of second moments
*
* %E
*******************************************************************************/
the rest of text
"""

if __name__ == "__main__":
    parser  = McStasComponentParser(config=testtext)


__date__ = "$Sep 15, 2010 3:05:52 PM$"


