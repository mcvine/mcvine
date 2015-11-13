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



def parse( stream, *args ):
    parser = create_parser()
    return parser.parse( stream, *args )


def parse_file( filename, *args ):
    return parse( open( filename ), *args )


def render( scatterer ):
    '''render(scatterer) --> text of the xml file

  - Inputs:
    scatterer: scatterer hierarchy
  - return: a list of strings
  '''
    renderer = create_renderer()
    class Options: pass
    options = Options()
    options.author = "Jiao Lin"
    options.organization = "Caltech"
    options.copyright = ""
    options.bannerWidth = 78
    options.bannerCharacter = '~'
    options.creator = ''
    options.timestamp = True
    options.lastLine = " End of file "
    options.copyrightLine = "(C) %s  All Rights Reserved"
    options.licenseText = ["{LicenseText}"]
    options.timestampLine = " Generated automatically by %s on %s"
    options.versionId = ' $' + 'Id' + '$'

    renderer.options = options

    text = renderer.render( scatterer )
    return text


def weave( scatterer, stream = None ):
    if stream is None:
        import sys
        stream = sys.stdout
        pass

    print >> stream, '\n'.join( render(scatterer) )
    return



def registerRendererExtension( extension_class ):
    renderer_extensions.append( extension_class )
    return


def removeRendererExtension( extension_class ):
    global renderer_extensions
    reg = renderer_extensions
    if extension_class in reg:
        del reg[ reg.index( extension_class ) ]
    return





def create_parser():
    from Parser import Parser
    parser = Parser()
    return parser


renderer_extensions = []
def create_renderer():
    from Renderer import Renderer
    klasses = [Renderer] + renderer_extensions
    klasses.reverse()
    klass = _inherit( klasses )
    # need Renderer.__init__
    klass.__init__ = Renderer.__init__
    return klass()

#helpers
def _inherit( klasses ):
    #print klasses
    P = klasses
    code = "class _( %s ): pass" % ','.join( [ 'P[%s]' % i for i in range(len(P)) ] )
    #print code
    exec code in locals()
    return _



# version
__id__ = "$Id$"

# End of file

