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

    lines = text.splitlines()
    Comments_dict = {}
    for l in lines:
         if l.startswith('#'):
            tmplst = l.split()
            if len(tmplst) > 1:
                ky=tmplst[1].strip()
                if ky.lower().startswith('atom'):
                    ky=ky+'_'+tmplst[2]
                if ky in Comments_dict.keys():
                    raise RuntimeError ("Duplicate Comment %s in laz file" %(tmplst[1]))
                Comments_dict[ky] = l
                if 'nb_atoms' in ky:
                    print(('\n key: '+ky+":"+Comments_dict[ky]+" \n"))

    class laz:
        lattice = getLattice(Comments_dict['CELL'])
        peaks = getPeaks(text, Comments_dict, lattice, line_width=line_width, dw_factor=dw_factor)
        cross_sections = getCrossSections(Comments_dict)
    return laz


def getCrossSections(comments):
    "obtain total cross sections"
    # This implementation assumes that there are following lines in the laz file
    # sigma_coh, sigma_inc, sigma_abs, nb_atoms
    # and use those to compute the total cross sections
    # It only works for single specie cases

    # get nb_atoms
    nb_atoms = int(comments['nb_atoms'].strip().split()[2])
    # sigma
    sigma_list = [x for x in comments.keys() if x.startswith('sigma')]
    assert len(sigma_list) == 3
    class xs: pass
    for sig_l in sigma_list:
        l=comments[sig_l]
        l = l[2:].strip()
        tokens = l.split()
        name = tokens[0]
        value = tokens[1]
        comment = ' '.join(tokens[2:])
        print((name, value, comment))
        assert comment[-6:] == '[barn]'
        setattr(xs, name[6:], float(value) * nb_atoms)
        continue
    # xs.coh, xs.inc, xs.abs
    return xs


def getPeaks(text, comments, lat, line_width=0, dw_factor=1):
    """
    Parse the peaks information from the laz file.
    """
    # figure out columns
    column_list = [x for x in comments.keys() if x.startswith('column')]
    # peaks records
    peaks = []


    p       = re.compile(COMMENT, re.DOTALL)    # Remove comments
    s       = re.sub(p, '', text)
    lines   = s.split("\n")
    col_idx={}
    for col in column_list:
        #print('\n\n line:'+comments[col]+'\n\n')
        col_idx[col] = int(comments[col].split()[2]) - 1

    for lin in lines:
        lin = lin.strip()
        if not lin:     # Empty line
            continue
        row = lin.split()
        peak = {}
        # this assumes integer hkl is there a case for non integer?
        h       = int(row[col_idx['column_h']])
        k       = int(row[col_idx['column_k']])
        l       = int(row[col_idx['column_l']])
        if 'column_F2' in column_list:
            F2 = float(row[col_idx['column_F2']])
        else:
            F = float(row[col_idx['column_F']])
            F2 = F*F
        mult    = int(row[col_idx['column_j']])    # Multiplicity
        q       = _q(lat, h, k, l)

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
    cell    = lines
    #assert cell.startswith('# CELL')
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
