#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2012  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

"""
parsers for diffraction data laz file

adapted from VULCAN/applications/peak_generator.py
"""


from math import pi as PI
from ..powder import Peak
import re


COMMENT = "(#[^\n]*\n)"  # Python comment


def parse(text, line_width=0, dw_factor=1):
    """parse given text of laz format and returns a list of peaks
    """
    text.replace("\r", "")  # Clean from CR

    lines   = text.splitlines()
    cell    = lines[1]      # Second lines should have lattice parameters
    assert cell.startswith('# CELL')
    cell    = cell.replace("#", "")
    par     = cell.split()

    # Parse lattice parameters: a, b, c, alpha, beta, gamma
    (_a, _b, _c, _alpha, _beta, _gamma) = \
         (float(par[1]), float(par[2]), float(par[3]),
          float(par[4]), float(par[5]), float(par[6]))
    # lattice
    import matter
    lat = matter.Lattice(_a, _b, _c, _alpha, _beta, _gamma)

    # peaks records
    peaks = []

    p       = re.compile(COMMENT, re.DOTALL)    # Remove comments
    s       = re.sub(p, '', text)
    lines   = s.split("\n")
    # XXX: positions are hard-coded!!!
    for l in lines:
        l       = l.strip()
        if not l:     # Empty line
            continue
        row     = l.split()
        peak    = {}
        h       = int(row[0])
        k       = int(row[1])
        l       = int(row[2])
        F       = float(row[12])      # F factor
        mult    = int(row[16])    # Multiplicity
        q       = _q(lat, h, k, l)
        F2      = F*F
        peak    = Peak(
            q = q, F_squared = F2,
            multiplicity = mult,
            intrinsic_line_width = line_width,
            DebyeWaller_factor = dw_factor,
            )
        peaks.append(peak)
        continue
    
    class laz:
        lattice = lat
        
    laz.peaks = peaks
    return laz


def _q(lattice, h, k, l):
    "Returns q from (h, k, l) parameters"
    import numpy
    rb      = lattice.recbase   # Reciprocal matrix
    # rb     = rb.T          # Should I transpose it?
    q       = 2*PI*(h*rb[0] + k*rb[1] + l*rb[2])
    return numpy.sqrt(numpy.dot(q,q))



# version
__id__ = "$Id$"

# End of file 
