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


class Header:

    def __init__(self, componentname, copyright, simple_description,
                 full_description, input_parameters, output_parameters,
                 ):
        self.componentname = componentname
        self.copyright = copyright
        self.simple_description =simple_description
        self.full_description = full_description
        self.input_parameters = input_parameters
        self.output_parameters = output_parameters
        return

    pass # end of Header


def parse( header_text ):
    ipos = header_text.find( '%I' )
    h = header_text[: ipos].splitlines()
    componentname = _parseHeaderOfHeader( h )
    
    dpos = header_text.find( '%D' )
    i = header_text[ipos : dpos].splitlines()
    copyright, simple_description = _parseInfo( i )
    
    ppos = header_text.find( '%P' )
    d = header_text[ dpos:ppos ].splitlines()
    full_description = _parseFullDescription( d )

    epos = header_text.find( '%E' )
    p = header_text[ ppos:epos ].splitlines()
    input_parameters, output_parameters = _parseParameters( p )
    return Header(
        componentname, copyright, simple_description,
        full_description, input_parameters, output_parameters,
        )


def _parseParameters( lines ):
    #remove '%P'
    lines = lines[1:]
    #look for "INPUT" and "OUTPUT"
    input_start = output_start = None
    input_sig = '* INPUT'
    output_sig = '* OUTPUT'
    for no, line in enumerate(lines):
        if line.startswith( input_sig ): input_start = no
        elif line.startswith( output_sig ): output_start = no
        else: pass
        continue
    if input_start is None or output_start is None:
        raise "Parameter section should have two sections: inputs and outputs.\n%s" % (
            '\n'.join(lines), )

    #remove '* '
    for no, line in enumerate(lines): lines[ no ] = line[ 2: ]
    
    inputs = lines[input_start+1: output_start]
    outputs = lines[output_start+1: ]

    input_parameters = _parseParameterList( inputs )
    output_parameters = _parseParameterList( outputs )
        
    return input_parameters, output_parameters


def _parseParameterList( params ):
    d = {}
    for p in params:
        p = p.strip()
        if p == '': continue
        try:
            name, description = p.split(':')
        except:
            raise ValueError, "Don't know how to parse %r" % (p,)
        name = name.strip()
        description = description.strip()
        d[name] = description
        continue
    return d


def _parseFullDescription( lines ):
    #remove '%D'
    lines = lines[1:]
    #remove '* '
    for no, line in enumerate(lines): lines[ no ] = line[ 2: ]
    lines = filter( lambda x: len(x.strip()), lines )
    return '\n'.join(lines)


def _parseHeaderOfHeader( h ):
    sig = '* Component:'
    for l in h:
        if l.startswith( sig ): return l[len(sig):].strip()
        continue
    raise "Cannot find component name in %s" % '\n'.join( h )


def _parseInfo( info ):
    #remove '%I'
    info = info[1:]
    #remove '* '
    for no, line in enumerate(info): info[ no ] = line[ 2: ]
    breaklineno = -1
    for no, line in enumerate(info):
        if line.strip() == '': breaklineno = no; break
        continue
    if breaklineno == -1:
        raise "This info only contains one paragraph: \n%s" % (
            '\n'.join( info ), ) 
    copyright = info[: breaklineno]
    simple_description = info[ breaklineno + 1: ]
    simple_description = filter( lambda x: len(x.strip()), simple_description )
    return '\n'.join(copyright), '\n'.join(simple_description)


testtext = """
/*******************************************************************************
*
* McStas, neutron ray-tracing package
*         Copyright 1997-2002, All rights reserved
*         Risoe National Laboratory, Roskilde, Denmark
*         Institut Laue Langevin, Grenoble, France
*
* Component: E_monitor
*
* %I
* Written by: Kristian Nielsen and Kim Lefmann
* Date: April 20, 1998
* Version: $Revision: 438 $
* Origin: Risoe
* Release: McStas 1.6
*
* Energy-sensitive monitor.
*
* %D
* A square single monitor that measures the energy of the incoming neutrons.
*
* Example: E_monitor(xmin=-0.1, xmax=0.1, ymin=-0.1, ymax=0.1, 
*                 Emin=1, Emax=50, nchan=20, filename="Output.nrj")
*
* %P
* INPUT PARAMETERS:
*
* xmin:     Lower x bound of detector opening (m)
* xmax:     Upper x bound of detector opening (m)
* ymin:     Lower y bound of detector opening (m)
* ymax:     Upper y bound of detector opening (m)
* Emin:     Minimum energy to detect (meV)
* Emax:     Maximum energy to detect (meV)
* nchan:    Number of energy channels (1)
* filename: Name of file in which to store the detector image (text)
*
* OUTPUT PARAMETERS:
*
* E_N:      Array of neutron counts
* E_p:      Array of neutron weight counts
* E_p2:     Array of second moments
*
* %E
*******************************************************************************/
"""

def test():
    header = parse( testtext )
    print header.componentname
    print header.copyright
    print header.simple_description 
    print header.full_description 
    print header.input_parameters 
    print header.output_parameters
    return


if __name__ == '__main__': test()

# version
__id__ = "$Id$"

# End of file 
