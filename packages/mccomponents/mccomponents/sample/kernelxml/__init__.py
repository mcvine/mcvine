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


from Parser import Parser
default_parser = Parser()


def parse( stream, *args ): return default_parser.parse( stream, *args )

def parse_file( filename, *args ): return parse( open( filename ), *args )


from Renderer import Renderer
default_renderer = Renderer()
def render( scatterer, renderer = None ):
    '''render(scatterer) --> text of the xml file

  - Inputs:
    scatterer: scatterer hierarchy
  - return: a list of strings
  '''
    if  renderer is None: renderer = default_renderer

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


# version
__id__ = "$Id$"

# End of file

