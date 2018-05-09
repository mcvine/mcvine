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
    # text.replace("\r", "")  # Clean from CR  # THIS LINE WAS NOT USEFUL
    
    lines   = text.splitlines()
    comments = [l for l in lines if l.startswith('#')]
    class laz:
        lattice = getLattice(comments)
        peaks = getPeaks(text, lattice, line_width=line_width, dw_factor=dw_factor)
        cross_sections = getCrossSections(comments)
    return laz


def getCrossSections(comments):
    "obtain total cross sections"
    # This implementation assumes that there are following lines in the laz file
    # sigma_coh, sigma_inc, sigma_abs, nb_atoms
    # and use those to compute the total cross sections
    # It only works for single specie cases
    
    # get nb_atoms
    s = [c for c in comments if c.startswith('# nb_atoms')]
    if not s: 
        raise IOError("Comments do not contain number of atoms in unit cell")
    if len(s) > 1:
        raise IOError("Comments contain more than one linesfor nb_atoms. Confused")
    nb_atoms = int(s[0][2:].strip().split()[1])
    
    # sigma
    signature = '# sigma'
    sigma_comments = [c for c in comments if c.startswith(signature)]
    assert len(sigma_comments) == 3
    class xs: pass
    for l in sigma_comments:
        l = l[2:].strip()
        tokens = l.split()
        name = tokens[0]
        value = tokens[1]
        comment = ' '.join(tokens[2:])
        print name, value, comment
        assert comment[-6:] == '[barn]'
        setattr(xs, name[6:], float(value) * nb_atoms)
        continue
    # xs.coh, xs.inc, xs.abs
    return xs


def getPeaks(text, lat, line_width=0, dw_factor=1):
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
    
    # sort peaks by q
    peaks = sorted(peaks, key=lambda p: p.q)
    return peaks


def _q(lattice, h, k, l):
    "Returns q from (h, k, l) parameters"
    import numpy
    rb      = lattice.recbase   # Reciprocal matrix
    # rb     = rb.T          # Should I transpose it?
    q       = 2*PI*(h*rb[0] + k*rb[1] + l*rb[2])
    return numpy.sqrt(numpy.dot(q,q))


def getLattice(lines):
    # !!! This demands that 2nd line contains lattice parameters
    cell    = lines[1]      # Second lines should have lattice parameters
    assert cell.startswith('# CELL')
    cell    = cell.replace("#", "")
    par     = cell.split()

    # Parse lattice parameters: a, b, c, alpha, beta, gamma
    (_a, _b, _c, _alpha, _beta, _gamma) = \
         (float(par[1]), float(par[2]), float(par[3]),
          float(par[4]), float(par[5]), float(par[6]))
    # lattice
    from diffpy.Structure import Lattice
    lat = Lattice(_a, _b, _c, _alpha, _beta, _gamma)
    return lat


# version
__id__ = "$Id$"

# End of file 
