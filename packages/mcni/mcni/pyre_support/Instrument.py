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


# constants

# number of simulation loops by default (ncount/buffer_size)
DEFAULT_NUMBER_SIM_LOOPS = 5
# minimum buffer size
MINIMUM_BUFFER_SIZE = 100



from MpiApplication import Application as base
from ParallelComponent import ParallelComponent

class Instrument( base, ParallelComponent ):

    class Inventory( base.Inventory ):

        import pyre.inventory
        
        #properties
        ncount = pyre.inventory.float('ncount', default = 10000)
        ncount.meta['tip'] = 'number of total neutrons generated by source'
        
        outputdir = pyre.inventory.str('output-dir', default = 'out')
        outputdir.meta['tip'] = 'output directory'

        overwrite_datafiles = pyre.inventory.bool(
            'overwrite-datafiles',  default = False)
        overwrite_datafiles.meta['tip'] = 'overwrite data files?'
        
        buffer_size = pyre.inventory.int  ('buffer_size', default = 0)
        buffer_size.meta['tip']= 'size of neutron buffer. This is for optimizing the preformance of the simulation. When it is too large, it will occupy too much memory. When it is too small, the simulation will be slow. If you are not sure, please just leave it unset so that the default value will be used.'

        from List import List
        sequence = List( 'sequence', default = '' )
        sequence.meta['tip'] = 'sequence of neutron components in this instrument'

        multiple_scattering = pyre.inventory.bool('multiple-scattering', default=False)
        multiple_scattering.meta['tip'] = 'if true, enable multiple scattering'

        #facilities

        #geometer. this is a place holder. should derive from Geometer
        #to create a new Geometer for the specific instrument.
        from Geometer import Geometer
        geometer = pyre.inventory.facility(
            'geometer', default = Geometer() )
        geometer.meta['tip'] = 'geometer of instrument'

        # tracer
        from NoNeutronTracer import NoNeutronTracer
        from NeutronTracerFacility import NeutronTracerFacility
        tracer = NeutronTracerFacility('tracer', default=NoNeutronTracer())

        # this option overrides "dumpconfiguration" to provide an iinterface
        # easier to use
        dumppml = pyre.inventory.str('dump-pml', default='')
        dumppml.meta['tip'] = "filename of output configuration (pml) file. if empty, ignored. if the given value is 'yes' or 'on', a default filename will be used."

        # XXX: to be removed
        # for backward compatibility
        dump_instrument = pyre.inventory.bool('dump-instrument')

        # dump registry to pkl file
        # this is for advanced users. the saved registry can be compared
        # to another saved registry, for example.
        dumpregistry = pyre.inventory.bool('dump-registry', default=False)
        dumpregistry.meta['tip'] = 'if true, dump the pyre registry to a pkl file'
        pass # end of Inventory


    def __init__(self, name):
        base.__init__(self, name)
        self._warning = journal.warning( name )
        return


    def help(self):
        print '------------------------------------------------------------'
        print '* Instrument simulation application %r' % self.name
        print '------------------------------------------------------------'
        print '* Sequence of components:'
        print '  ', self._componentListStr()
        print '------------------------------------------------------------'
        print '* Command:'
        print self._cmdlineDemoStr()
        print '------------------------------------------------------------'
        return


    def main(self, *args, **kwds):
        if self.inventory.dumpregistry:
            self._dumpRegsitry()
            return
        
        import mcni
        instrument = self._createInstrument()
        
        geometer = self.geometer

        multiple_scattering = self.inventory.multiple_scattering
        tracer = self.tracer
        
        n = int(self.ncount / self.buffer_size)
        assert n>0, 'ncount should be larger than buffer_size: ncount=%s, buffer_size=%s' % (self.ncount, self.buffer_size)
        
        for i in range(n):
            neutrons = mcni.neutron_buffer( self.buffer_size )
            mcni.simulate( instrument, geometer, neutrons, 
                           multiple_scattering=multiple_scattering,
                           tracer = tracer)
            continue
        
        remain = int(self.ncount % self.buffer_size)
        if remain:
            neutrons = mcni.neutron_buffer(remain)
            mcni.simulate( instrument, geometer, neutrons, 
                           multiple_scattering=multiple_scattering,
                           tracer = tracer)

        import os
        print os.times()
        return


    def _dumpRegsitry(self):
        out = '%s-reg.pkl' % self.name
        import os
        if os.path.exists(out):
            raise RuntimeError, 'dump registry: path %s already exists' % out

        from pyre.applications.Application import retrieveConfiguration
        reg = self.createRegistry()
        retrieveConfiguration(self.inventory, reg)
        from RegistryToDict import Renderer
        renderer = Renderer()
        reg = renderer.render(reg)
        
        import pickle
        pickle.dump(reg, open(out, 'w'))
        return


    def _createInstrument(self):
        neutron_components = self.neutron_components
        for comp in neutron_components:
            if comp not in self.sequence:  
                self._warning.log(
                    'component %s was not included in component sequence %s' % (
                    comp, self.sequence )
                    )
                pass
            continue
        
        for name in self.sequence:
            if name not in neutron_components:
                raise RuntimeError , "Neutron component %s specified in sequence %s does not " \
                      "correspond to any known simulation components: %s" % (
                    name, self.sequence, neutron_components )
            continue

        import mcni
        components = [ neutron_components[ name ] for name in self.sequence ]
        instrument = mcni.instrument( components )
        return instrument
    
    
    def _defaults(self):
        base._defaults(self)
        self.inventory.geometer = _build_geometer( self )
        return
    
    
    def _setup_ouputdir(self):
        outputdir = self.outputdir
        if not self.overwrite_datafiles and os.path.exists( outputdir ):
            print "output directory %r exists. If you want to overwrite the output "\
                  "directory, please specify option --overwrite-datafiles." % outputdir

        if not os.path.exists( outputdir ):
            os.makedirs( outputdir )
            pass

        for component in self.neutron_components.itervalues():
            component.setOutputDir( outputdir )
            if self.parallel:
                # need to let the master node component know the "master" outputdir
                if self.mpiRank == 0:
                    component._master_outputdir = self.inventory.outputdir
            component.overwrite_datafiles = self.overwrite_datafiles
            continue
        
        return
    
    
    def _configure(self):

        # XXX: to be removed
        # XXX: for backward compatibility
        dump_instrument = self.inventory.dump_instrument
        if dump_instrument:
            import warnings
            warnings.warn('This option is not supported anymore. Please use --dump-pml')
        
        # handle dumppml
        # this overrides the option dumpconfiguration in order to
        # provide a simpler interface for users.
        dumppml = self.inventory.dumppml
        if dumppml:
            self.inventory.dumpconfiguration = True

        base._configure(self)
        self.geometer = self.inventory.geometer
        self.overwrite_datafiles = self.inventory.overwrite_datafiles

        self.outputdir = self.inventory.outputdir
        if self.parallel:
            ext = self._outputdir_mpiext()
            self.outputdir = '%s-%s' % (self.outputdir, ext)
            
        self.sequence = self.inventory.sequence
        self.buffer_size = self._getBufferSize()
        self.ncount = self.inventory.ncount
        if self.parallel:
            # every node only need to run a portion of the total counts
            partitions = getPartitions(self.ncount, self.mpiSize)
            self.ncount = partitions[self.mpiRank]

        neutron_components = {}
        for name in self.inventory.facilityNames():
            comp = self.inventory.getTraitValue( name )
            if self._showHelpOnly:
                comp._showHelpOnly = True
            if isinstance(comp, McniComponent):
                neutron_components[ name ] = comp
                pass
            continue

        self.neutron_components = neutron_components

        # tracer
        tracer = self.inventory.tracer
        if tracer.name == 'no-neutron-tracer':
            tracer = None
        self.tracer = tracer
        
        # if in server mode for parallel computing
        # we actually don't want the subcomponents to
        # initialize, because in the "server" mode 
        # the application just call launcher to 
        # let workers start working.
        # this logic probably should go into class MpiApplication.
        # Please read MpiApplication._init as well!
        from MpiApplication import usempi
        noinit = usempi \
            and (self.inventory.launcher.nodes > 1) \
            and self.inventory.mode == 'server'
        for c in neutron_components:
            comp = self.inventory.getTraitValue(c)
            comp._noinit = noinit            

        if not self._showHelpOnly: self._setup_ouputdir()
        return


    def _getBufferSize(self):
        # user requested size
        usersize = self.inventory.buffer_size
        # 
        if not usersize:
            return self._computeBufferSize()

        maxsize = self._maximumBufferSize()
        if usersize > maxsize:
            return maxsize

        minsize = self._minimumSuggestedBufferSize()
        if usersize < minsize:
            import warnings
            warnings.warn("The buffer size %s is too small" % usersize)
            
        return usersize


    def _minimumSuggestedBufferSize(self):
        return self.inventory.ncount / 1000 / (self.mpiSize or 1)


    def _computeBufferSize(self):
        ncount = self.inventory.ncount
        mpisize = self.mpiSize or 1
        nsteps = DEFAULT_NUMBER_SIM_LOOPS
        return min(self._maximumBufferSize(), int(ncount/nsteps/mpisize))


    def _maximumBufferSize(self):
        import psutil
        memsize = min(psutil.TOTAL_PHYMEM/2, (psutil.avail_phymem() + psutil.avail_virtmem())*0.7)
        memsize = int(memsize)
        from mcni.neutron_storage.idfneutron import ndblsperneutron
        
        bytesperdble = 8
        minsize = MINIMUM_BUFFER_SIZE
        
        n = int(memsize/ndblsperneutron/bytesperdble/minsize)*MINIMUM_BUFFER_SIZE

        if n<minsize:
            raise RuntimeError, "Not enough memory"
        
        return n


    def _saveConfiguration(self):
        # the default configuration filename
        default_filename = '%s.pml' % self.name
        
        # the given filename
        dumppml = self.inventory.dumppml
        if dumppml in ['yes', 'on']:
            outfile = default_filename
        else:
            outfile = dumppml

        # make sure the output path does not exist
        import os
        if os.path.exists(outfile):
            raise RuntimeError, "output file %r already exists" % outfile

        # get registry
        registry = self.createRegistry()
        exclude_props = [
            'weaver',
            'typos',
            'dumpconfiguration', 'dumpconfiguration-output',
            'help-properties', 'help', 'help-persistence', 'help-components',
            'dump-pml',
            ]
        from pyre.applications.Application import retrieveConfiguration
        registry = retrieveConfiguration( 
            self.inventory, registry, excludes=exclude_props)
        
        # the output stream
        stream = open(outfile, 'w')

        # weave
        self.weaver.weave( registry, stream )

        # footer
        stream.write('<!-- \n automatically created by the following command:\n')
        cmd = _getCmdStr()
        stream.write(' $ %s\n' % cmd)
        stream.write('-->\n\n')

        # give a warning when use non-default config filename
        import os, sys
        base = os.path.basename(outfile)
        if base != default_filename:
            print '*'*70
            print "Warning: you will need to rename file %s to %s, otherwise this file won't be used by the simulation application %s" % (
                outfile, default_filename, os.path.basename(sys.argv[0]))
            print '*'*70
        return
    
    
    def _outputdir_mpiext(self):
        mode = self.inventory.mode
        rank = self.mpiRank
        return '%s-%s' % (mode, rank)


    def _componentListStr(self):
        comps = self.neutron_components
        l = []
        for name in self.inventory.sequence:
            comp = comps[name]
            if hasattr(comp, 'uri'): uri = comp.uri
            else: uri = comp.name
            l.append( (name, uri) )
            continue
        return ' --> '.join(['[%s(%s)]' % (n, u) for n,u in l])
        

    def _cmdlineDemoStr(self):
        s = ' $ %s ' % self.name
        opts = []
        skipappprops=['name', 'typos', 'journal', 'geometer', 'sequence', 'weaver']+\
            self.inventory.sequence

        from _invutils import getComponentPropertyNameTipPairs
        appopts = getComponentPropertyNameTipPairs(self, skipappprops)
        opts += [(n, '<%s>'%tip) for n, tip in appopts]
        for comp in self.inventory.sequence:
            opts.append( ('geometer.%s' % comp, '<position>,<orientation>') )
            continue
        for name in self.inventory.sequence:
            opts.append( (name, '<component type>') )
            continue
        components = self.neutron_components
        for name in self.inventory.sequence:
            comp = components[name]
            pairs = getComponentPropertyNameTipPairs(comp)
            pairs = [ ('%s.%s' % (name, n), '<%s>' % tip) for n, tip in pairs]
            opts += pairs
            continue
        l = [s] + ['  --%s=%s' % (k,v) for k, v in opts]
        return ' \\\n'.join(l) 


    # overwrite processCommandline so that we know
    # user is requesting for help and avoid unecessary
    # initialization and finalization of components
    def processCommandline(self, registry):
        ret = super(Instrument, self).processCommandline(registry)
        help = ret[0]
        if help: self._showHelpOnly = True
        return ret
    

    pass # end of Instrument



def _getCmdStr():
    import sys, os
    argv = list(sys.argv)
    argv[0] = os.path.basename(argv[0])
    for i,t in enumerate(argv):
        if t.startswith('--'): argv[i] = '-'+t[2:]
        continue
    return ' '.join(argv)


def _build_geometer( instrument ):
    from _geometer_utils import buildGeometerFromInventory
    Inventory = instrument.Inventory
    g = buildGeometerFromInventory(Inventory)
    g.instrument = instrument
    return g
    

def getPartitions(N, n):
    return list(getPartitionIterator(N,n))

def getPartitionIterator( N, n ):
    '''create an iterator of n partitions where the sum of all partions is N
    All partitions should be about the same size.
    '''
    from math import ceil
    residual = N
    nbins = n
    while residual:
        if nbins > 1:
            size = int( ceil(residual*1./nbins) )
        else:
            size = residual
        yield size
        residual -= size
        nbins -= 1
    return 


from mcni.AbstractComponent import AbstractComponent as McniComponent
import os, journal


# version
__id__ = "$Id$"

# End of file 
