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


def sampleassembly2compositescatterer( sampleassembly ):
    return SampleAssembly2CompositeScatterer().render( sampleassembly )



def findkernelsfromxmls( compositescatterer ):
    return FindKernelsFromXMLs().render( compositescatterer )



class SampleAssembly2CompositeScatterer:

    '''render a composite scatterer reperesentation
    (svn://danse.us/MCViNE/.../mccomposite)
    from
    a sample assembly representation
    (svn://danse.us/inelastic/sample/.../sampleassembly)
    '''

    def render(self, sampleassembly):
        return sampleassembly.identify(self)


    def onSampleAssembly(self, sampleassembly ):
        #
        lg = sampleassembly.local_geometer

        # the container
        import mccomposite
        compositeScatterer = mccomposite.composite( )

        for scatterer in sampleassembly.elements():
            s = scatterer.identify(self)
            p = lg.position( scatterer )
            o = lg.orientation( scatterer )
            compositeScatterer.addElement( s, p, o )
            continue

        return compositeScatterer


    def onHomogeneousScatterer(self, scatterer ):
        import mccomponents.homogeneous_scatterer as hs
        s = hs.homogeneousScatterer( scatterer.shape(), kernel = None )
        s.origin = scatterer
        return s


    onPowderSample = onHomogeneousScatterer

    pass # end of SampleAssembly2CompositeScatterer



#go thru the scatterer composite tree and
#find kernel xmls and load them.
#each scatterer has an "origin" attached, and that "origin"
#is a node of "sampleassembly" package (svn://danse.us/inelastic/sample/.../sampleassembly).
#Basisically, the scatterer composite tree is a result of SampleAssembly2CompositeScatterer.
class FindKernelsFromXMLs:
    
    def render(self, compositescatterer):
        return compositescatterer.identify(self)


    def onCompositeScatterer(self, compositescatterer):
        for scatterer in compositescatterer.elements():
            scatterer.identify(self)
            continue
        return compositescatterer


    def onHomogeneousScatterer(self, scatterer):
        origin = scatterer.origin
        name = origin.name
        xmlfilename = '%s-scatteringkernel.xml' % name
        from kernelxml import parse_file
        kernel = parse_file( xmlfilename, scatterer )
        #scatterer.setKernel( kernel )
        kernel.scatterer_origin = origin
        return


    onPowderSample = onHomogeneousScatterer

    pass # end of FindKernelsFromXMLs


# version
__id__ = "$Id$"

# End of file 
