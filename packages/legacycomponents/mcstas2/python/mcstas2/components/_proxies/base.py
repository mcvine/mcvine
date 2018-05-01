from ...AbstractComponent import AbstractComponent
from mcni.components.ParallelComponent import ParallelComponent

class Component(AbstractComponent, ParallelComponent):

    def __init__(self, cpp_instance_factory, *args, **kwds):
        # args, if exists, must be "name"
        assert len(args) in [0, 1]
        if args: kwds['name' ] = args[0]
        for k, v in kwds.items():
            setattr(self, k, v)
        # self._cpp_instance is an instance created
        # by factory methods auto-generated from mcstas components
        # see template code in mcstas2.wrappers.pymodule.factorymethod_py
        self._cpp_instance = cpp_instance_factory(**kwds)
        self.restore_neutron = False
        self._cpp_instance_factory = cpp_instance_factory
        return
    

    def process(self, neutrons):
        restore_neutron = self.restore_neutron
        if restore_neutron:
            # create a copy to be processed
            saved = neutrons.snapshot(len(neutrons))
            
        # and process neutrons as normal
        ret = self._cpp_instance.process(neutrons)
    
        # dump all calculated data
        self._dumpData()
        
        # restore neutrons if requested
        if restore_neutron:
            neutrons.swap(saved)
            
        return ret


    def _dumpData(self):
        return


# End of file 
