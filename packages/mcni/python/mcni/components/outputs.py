#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


"""
assumption:
 in each round the simulation spits out something to a output-directory-in-progress.

  <outdir>/<signature-of-progress>/<some files>

e.g.

  out/rank0-step3/number_of_mc_samples

"""


number_mc_samples_filename = 'number_of_mc_samples'

import glob, os
def mcs_sum(outdir):
    """compute the summed number of mc samples"""
    files = mcsamples_files(outdir)
    if not files:
        return 0
    # load number_of_mc_samples
    loadmcs = lambda f: float(open(f).read())
    mcs = list(map(loadmcs, files))
    return sum(mcs)


def mcsamples_files(outdir):
    pattern = os.path.join(outdir, '*', number_mc_samples_filename)
    return glob.glob(pattern)


def n_mcsamples_files(outdir):
    return len(mcsamples_files(outdir))


# version
__id__ = "$Id$"

# End of file 
