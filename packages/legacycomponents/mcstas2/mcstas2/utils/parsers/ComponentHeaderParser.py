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
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# modified by Alta Fang 7/7/09

from pyparsing.pyparsing import *

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
    # first strip away the stars and put into string called starlesstext
    starlesstext = ""
    aline = Optional(Suppress("*") + restOfLine.setResultsName("restofline"))
    for l in header_text.splitlines():
        if l.find("*") != -1:
            starlesstext += aline.parseString( l ).restofline + "\n"
        else:
            starlesstext += l + "\n"
    
    # Define what blocks of text are, for parsing later
    words = ZeroOrMore(Word(alphanums + """\/_-()^[]<>@,.=$&+*":;\n'"""))
    textFormat = Combine(words, joinString=" ", adjacent=False)
    
    # Parse component name
    componentInfo = "Component:" + Word(alphanums + "_").setResultsName("componentname") \
                    + Optional("." + textFormat)
    try:
        component_name = componentInfo.searchString(starlesstext)[0].componentname
    except:
        #raise Exception("Cannot find component name in header")
        component_name = None
    
    # Parse copyright and simple description  
    copyrightAndDescripInfo = "%I" + SkipTo(lineEnd) \
                               + textFormat.setResultsName("copyrightAndDescrip")
    copyrightAndDescripList = copyrightAndDescripInfo.searchString(starlesstext)
    copyrightAndDescrip = copyrightAndDescripList[0].copyrightAndDescrip
        
    # Parse full description
    descriptionInfo = "%D" + SkipTo(lineEnd) + textFormat.setResultsName("full_description")
    full_description = descriptionInfo.searchString(starlesstext)[0].full_description

    # Parse parameters, separately
    parameterInfo = "%P" + SkipTo(lineEnd) + textFormat.setResultsName("parameters")  
    parsedParams = parameterInfo.searchString(starlesstext)[0]
    parameterBlock = parsedParams.parameters 
    
    # Define way to split strings that are separated by extra newlines: 
    def mustBeNonBlank(s,l,t):
        if not t[0]:
            raise ParseException(s,l,"line body can't be empty")
    lineBody = SkipTo(lineEnd).setParseAction(mustBeNonBlank)
    textLine = lineBody + Suppress(lineEnd).setParseAction(replaceWith("\n"))
    para = OneOrMore(textLine) + Suppress(lineEnd)

    # Split copyright and simple description, if applicable
    splitPara = para.searchString(copyrightAndDescrip)
    copyright = "".join(splitPara[0])
    simple_description = None  
    try:
        simple_description = splitPara[1][0]
    except:
        pass

    # Split parameters into input and output, and make them into dictionaries
    input_ident = CaselessLiteral("INPUT PARAMETERS") + Optional(":")
    output_ident = CaselessLiteral("OUTPUT PARAMETERS") + Optional(":")
    optional_ident = CaselessLiteral("OPTIONAL PARAMETERS") + Optional(":")
    end_input = output_ident ^ optional_ident
    paramWord = Word(alphanums + """ *\/_-()[]^<>@+,.=$&":'""")
    param_block = Group(ZeroOrMore(~output_ident + paramWord))
    total_params = Optional(input_ident) + Group(ZeroOrMore(~end_input \
                  + paramWord)).setResultsName("input_parameters") + Optional(optional_ident + param_block) \
              + Optional(output_ident + textFormat.setResultsName("output_parameters")) + StringEnd()
    splitParams = total_params.searchString(parameterBlock)[0]    
    input_parameters = makeDictionary("\n".join(splitParams.input_parameters))
    if splitParams.output_parameters != None:
        output_parameters = makeDictionary(splitParams.output_parameters)   
    else:
        output_parameters = None

    # Finally, return a Header object
    return Header(component_name, copyright, simple_description,  \
                 full_description, input_parameters, output_parameters)

# Function to put parameters that are in a string into a dictionary
def makeDictionary(text):
    d = {}
    okword = Word(alphanums + """\/_-()[]<>+@,.=:$&'"^ """)
    okvar = Word(alphanums + """\/_-()[]<>+@,.=$&'"^ """)
    block = Combine(ZeroOrMore(okword))
    aline = Combine(ZeroOrMore(okvar)).setResultsName("first") + Literal(":") \
            + block.setResultsName("second") + LineEnd()
    aUnit = aline + Optional(Combine(Combine(ZeroOrMore(okvar), joinString=" ", \
            adjacent=False).setResultsName("secondContinued") + LineEnd()))
    parsedVars = aUnit.searchString(text)
    for unit in parsedVars:
        d[unit.first] = unit.second + " " + unit.secondContinued
    return d

testtext = """
/*******************************************************************************
*
*
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

# Test the parsing
if __name__ == "__main__":
    results = parse(testtext)
    print "component:", results.componentname
    print "copyright:", results.copyright
    print "simple description:", results.simple_description
    print "full description:", results.full_description
    print "input parameters:", results.input_parameters
    print "output parameters:", results.output_parameters
    
