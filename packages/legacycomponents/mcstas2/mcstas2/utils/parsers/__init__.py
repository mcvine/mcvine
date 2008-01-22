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


def parseComponent( component_file ):
    from ComponentParser import component as componentParser
    parser = componentParser()
    s = open(component_file).read()
    info = parser.parseString( s )

    from ComponentHeaderParser import parse
    header = parse( info.header )

    assert header.componentname == info.name
    name = info.name

    inputParamDescs = header.input_parameters
    outputParamDescs = header.output_parameters

    definition_parameters = _addDescription( info.definition_parameters, inputParamDescs )
    setting_parameters = _addDescription( info.setting_parameters, inputParamDescs )
    output_parameters = _addDescription( info.output_parameters, outputParamDescs )

    state_parameters = info.state_parameters
    
    from ComponentInfo import ComponentInfo
    return ComponentInfo(
        name,
        header.copyright, header.simple_description,
        header.full_description, 
        definition_parameters,
        setting_parameters,
        output_parameters,
        state_parameters,
        info.declare,
        info.initialize, info.trace, info.save, info.finalize
        )


def _addDescription( parameters, descriptions ):
    from ComponentInfo import Parameter
    ret = []
    for param in parameters:
        name = param.name
        d = descriptions.get( name ) or ''
        p = Parameter( name, param.type, param.value, d )
        ret.append( p )
        continue
    return ret
    

# version
__id__ = "$Id$"

# End of file 
