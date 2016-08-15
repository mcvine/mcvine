# -*- Python -*-
# 
# Jiao Lin <jiao.lin@gmail.com>
#


'''
factory to create an instrumnt pyre application class
from a list of component names.
'''

import os


def build(neutron_components):
    
    class _Proxy:
        """proxy class of instrument sim app"""
        
        def __init__(self, *args, **kwds):
            self._init_params = args, kwds
            return

        def run(self, *args, **kwds):
            raise NotImplementedError
    
    _Proxy.neutron_components = neutron_components
    return _Proxy


def _build(neutron_components):
    
    from mcni.pyre_support.Instrument import Instrument as base
    class Instrument(base):

        class Inventory( base.Inventory ):

            from mcni.pyre_support import facility, componentfactory as component
            import mccomponents.pyre_support

            for name in neutron_components:
                code = '%s = facility("%s", default="mcni://optics/Dummy" )' % (
                    name, name)
                exec code in locals()
                continue
            del code, name

            import pyre.inventory as pinv
            # path of the post processing script
            # the components that need post-processing should append
            # to this script
            post_processing_script = pinv.str("post-processing-script")

            pass # end of Inventory


        def _defaults(self):
            base._defaults(self)
            self.inventory.sequence = neutron_components
            pps = self.inventory.post_processing_script
            if not pps:
                pps = os.path.join(self.inventory.outputdir, 'post-processing-script.py')
            self.post_processing_script = pps
            return


        def _makeSimContext(self):
            context = base._makeSimContext(self)
            context.post_processing_script = self.post_processing_script
            return context

        pass # end of Instrument

    return Instrument


# End of file 
