#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C)   2007    All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode, debug


class GridSQE(AbstractNode):


    tag = "GridSQE"

    def elementFactory( self, **kwds ):
        datapath = kwds.get('idf-data-path')
        hdfpath = kwds.get('histogram-hdf-path')
        if datapath:
            from mccomponents.sample.idf import readSQE
            sqe = readSQE( datapath )
            pass
        elif hdfpath:
            from histogram.hdf import load
            try:
                sqe = load( hdfpath )
            except:
                import os, traceback
                f = os.path.dirname(hdfpath)
                e = os.path.basename(hdfpath)
                t = traceback.format_exc()
                raise IOError, "unable to load histogram from hdf5 file %s, entry %s. Original traceback:\n%s" % (f, e, t)
            pass
        else:
            raise ValueError, "GridSQE needs path to "\
                  "idf data files or "\
                  "histogram hdf5 file "

        auto_normalization = kwds.get('auto-normalization')
        if auto_normalization:
            auto_normalization = auto_normalization.lower()
            trues = ['on', 'yes', '1', 'true']
            falses = ['off', 'no', '0', 'false']
            if auto_normalization in trues:
                auto_normalization = True
            elif auto_normalization in falses:
                auto_normalization = False
            else:
                raise ValueError("Unrecognized value for auto-normalization: %s" % auto_normalization)
                
        if auto_normalization:
            norm = _calcNorm(sqe)
            if abs(norm-1) > 0.2:
                sqe.I /= norm
        from mccomponents.sample import gridsqe
        return gridsqe( sqe )

    pass # end of GridSQE


def _calcNorm(sqe):
    I = sqe.I
    Q = sqe.Q
    I1 = I.copy()
    for i in range(len(Q)):
        I1[i] *= Q[i]
        continue
    import numpy
    return numpy.average(I1)


# version
__id__ = "$Id$"

# End of file 
