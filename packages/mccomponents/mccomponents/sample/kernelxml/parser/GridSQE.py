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
                raise IOError, "unable to load histogram from file %s, entry %s. Original traceback:\n%s" % (f, e, t)
            pass
        else:
            raise ValueError, "GridSQE needs path to "\
                  "idf data files or "\
                  "histogram hdf5 file "
        
        from mccomponents.sample import gridsqe
        return gridsqe( sqe ) 

    pass # end of GridSQE


# version
__id__ = "$Id$"

# End of file 
