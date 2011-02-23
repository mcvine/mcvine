#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2011 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#

# common interface for vitess component


VITESS_NEUTRON_SIZE=108


import os


from mcni.AbstractComponent import AbstractComponent
class Component(AbstractComponent):

    vitessmodulespath = os.environ.get('VITESS_MODULES_DIR')
    if not vitessmodulespath:
        raise RuntimeError, "Cannot find vitess modules. please set env var VITESS_MODULES_DIR"

    def __init__(self, name, modulename=None, parameters={}):
        super(Component, self).__init__(name)
        self.modulename = modulename
        self.parameters = parameters
        return


    def process(self, neutrons):
        vnb = neutronbuffer2vitess(neutrons)
        cmd = [os.path.join(self.vitessmodulespath, self.modulename)]
        cmd += ['-%s %s' % (k,v) for k,v in self.parameters]
        cmd = ' '.join(cmd)
        p = sp.Popen(cmd, stdin=sp.PIPE)
        out, err = p.communicate(vnb.getCharPtr())
        rt = p.wait()
        if rt:
            raise RuntimeError, "%s failed" % cmd
        n = len(out)/VITESS_NEUTRON_SIZE
        neutrons.resize(n)
        vitessbuffer2mcvinebuffer(out, n, neutrons)
        return

    
from vitessbp import neutronbuffer2vitess, vitessbuffer2mcvinebuffer
import subprocess as sp
    
# version
__id__ = "$Id$"

# End of file 
