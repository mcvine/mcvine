#!/usr/bin/env python
#
# Jiao Lin <jiao.lin@gmail.com>
#

"""
parsers for diffraction data lau file

adapted from laz.py
"""


from math import pi as PI
import re
from ..singlecrystal import HKL

COMMENT = "(#[^\n]*\n)"  # Python comment


def parse(text):
    """parse given text of lau format and returns a list of peaks
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
                    raise RuntimeError ("Duplicate Comment %s in lau file" %(tmplst[1]))
                Comments_dict[ky] = l
                if 'nb_atoms' in ky:
                    print(('\n key: '+ky+":"+Comments_dict[ky]+" \n"))
        continue
    class lau:
        lattice = getLattice(Comments_dict['CELL'])
        hkls = getHKLs(text, Comments_dict, lattice)
    return lau


def getHKLs(text, comments, lat):
    """
    Parse the peaks information from the lau file.
    """
    # figure out columns
    column_list = [x for x in comments.keys() if x.startswith('column')]
    col_idx={}
    for col in column_list:
        #print('\n\n line:'+comments[col]+'\n\n')
        col_idx[col] = int(comments[col].split()[2]) - 1
    # hkl records
    hkls = []
    # remove comments
    p       = re.compile(COMMENT, re.DOTALL)
    s       = re.sub(p, '', text)
    #
    lines   = s.split("\n")
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
        F2 = float(row[col_idx['column_F2']])
        # print(row)
        # print(h,k,l,F2)
        hkl    = HKL(hkl=(h,k,l), F_squared=F2)
        hkls.append(hkl)
        continue
    return hkls


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

# End of file
