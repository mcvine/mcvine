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
PyreStripper - takes pyre command line script and strips parameters that are empty!

Example session:
    $ python pyrestripper.py -f=../tests/teststripper.txt

Note:
    - Each parameter should be on a separate line
"""

import re
import sys

EMPTYSTR    = "=(\"\"|''|[ ]+|\\\\)"
FILE        = ["--filename", "-f"]

class PyreStripper:

    def __init__(self, filename):
        self._filename  = filename
        self._lines     = []
        linesbefore     = open(filename).readlines() # Doesn't check if file exists
        self.strip(linesbefore)


    def strip(self, lines):
        "Strips empty parameter"
        p           = re.compile(EMPTYSTR) # on one line only
        filtered    = []
        for l in lines:
            m       = p.findall(l)
            if not m:   # not empty
                filtered.append(l)

        self._lines = filtered


    def toString(self):
        return "".join(self._lines)


def main():
    stripper    = None
    for arg in sys.argv:
        parts   = arg.split("=")
        key     = parts[0]
        if key in FILE:
            print parts
            stripper    = PyreStripper(filename=parts[1])

    if not stripper:
        return

    print stripper.toString()


if __name__ == "__main__":
    main()


__date__ = "$Oct 13, 2010 2:14:30 PM$"


