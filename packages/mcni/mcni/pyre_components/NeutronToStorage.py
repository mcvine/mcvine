#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2007  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


# Every directory containing neutron data files must have a
# text file stating the number of neutrons in each neutron data
# file.
packetsizefile = 'packetsize'


from mcni.neutron_storage import ndblsperneutron

from mcni.pyre_support.AbstractComponent import AbstractComponent

class NeutronToStorage( AbstractComponent ):


    class Inventory( AbstractComponent.Inventory ):
        import pyre.inventory as pinv
        path = pinv.str( 'path', default = '' )
        append = pinv.bool( 'append', default = False )
        pass
    

    def process(self, neutrons):
        path = self.path
        
        n = len(neutrons)

        packetsize = self._getpacketsize()
        if packetsize is None:
            self._setpacketsize( n )
            packetsize = n
            pass

        if n != packetsize:
            raise RuntimeError , "packet size in %r is %d, "\
                  "but neutron buffer has size %d" % (
                path, packetsize, n )

        filename = self._uniquefilename()
        from mcni.neutron_storage import dump
        dump(neutrons, os.path.join( path, filename ) )
        return neutrons
    
    
    def _getpacketsize(self):
        p = os.path.join( self.path, packetsizefile )
        if not os.path.exists( p ): return
        return long( open(p).read() )


    def _setpacketsize(self, n):
        p = os.path.join( self.path, packetsizefile )
        open(p, 'wt').write( '%s' % n )
        return


    def _uniquefilename(self):
        entries = os.listdir( self.path )
        numbers = []
        for entry in entries:
            try: n = int( entry )
            except: continue
            numbers.append( n )
            continue
        if len(numbers) == 0: return '0'
        return str( max(numbers) + 1 )
    

    def _configure(self):
        AbstractComponent._configure(self)
        self.path = self.inventory.path
        return


    def _init(self):
        AbstractComponent._init(self)

        path = self.path = os.path.abspath( self.path )

        if os.path.exists( path ):
            msg = 'path %r already exists. if you want to append neutron event files to '\
                  'that directory, please set "append" to True' % path
            if not self.inventory.append: raise msg
            pass
        
        if not os.path.exists( path ): os.makedirs( path )
        
        if not os.path.isdir( path ):
            raise IOError , "path %r is not a directory" % path

        return

    pass # end of Source


def filesize( n ):
    '''calculate neutron file size given number of neutrons
    '''
    return titlesize + versionsize + commentsize + nsize + n * neutronsize


import os, math, numpy


# version
__id__ = "$Id$"

# End of file 
