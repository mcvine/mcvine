#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                 Jiao Lin   
#                      California Institute of Technology
#                      (C) 2006-2010  All Rights Reserved
#
# <LicenseText>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from AbstractNode import AbstractNode, debug


class E_Q_Kernel(AbstractNode):


    tag = "E_Q_Kernel"

    def elementFactory( self, **kwds ):
        from mccomponents.sample import E_Q_Kernel
        # E_Q = self._parse( kwds['E_Q'] )
        # S_Q = self._parse( kwds['S_Q'] )
        E_Q = str(kwds['E_Q'])
        S_Q = str(kwds['S_Q'])
        Qmin = self._parse( kwds['Qmin'] )
        Qmax = self._parse( kwds['Qmax'] )
        return E_Q_Kernel(E_Q=E_Q, S_Q=S_Q, Qmin=Qmin, Qmax=Qmax)
    
    
    pass # end of E_Q_Kernel


# version
__id__ = "$Id: E_Q_Kernel.py 601 2010-10-03 19:55:29Z linjiao $"

# End of file 
