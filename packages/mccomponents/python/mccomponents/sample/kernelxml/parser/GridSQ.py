#!/usr/bin/env python
#
#


from AbstractNode import AbstractNode, debug


class GridSQ(AbstractNode):


    tag = "GridSQ"

    def elementFactory( self, **kwds ):
        hdfpath = kwds.get('histogram-hdf-path')
        from histogram.hdf import load
        try:
            sq = load( hdfpath )
        except:
            import os, traceback
            f = os.path.dirname(hdfpath)
            e = os.path.basename(hdfpath)
            t = traceback.format_exc()
            raise IOError, "unable to load histogram from hdf5 file %s, entry %s. Original traceback:\n%s" % (f, e, t)
        from mccomponents.sample import gridsq
        return gridsq( sq )

    pass # end of GridSQ


# End of file 
