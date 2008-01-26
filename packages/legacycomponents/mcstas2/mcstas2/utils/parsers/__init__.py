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

    name = '%s' % info.name    
    assert header.componentname == info.name

    inputParamDescs = header.input_parameters
    outputParamDescs = header.output_parameters

    definition_parameters = _addDescription( info.definition_parameters, inputParamDescs )
    setting_parameters = _addDescription( info.setting_parameters, inputParamDescs )
    output_parameters = _addDescription( info.output_parameters, outputParamDescs )

    state_parameters = [ str(p) for p in info.state_parameters ]

    full_description = header.full_description.replace(
        name+'(', name+'(name, ')
    
    from ComponentInfo import ComponentInfo
    return ComponentInfo(
        name,
        header.copyright, header.simple_description,
        full_description,
        definition_parameters,
        setting_parameters,
        output_parameters,
        state_parameters,
        '%s' % info.declare,
        '%s' % info.initialize, '%s' % info.trace,
        '%s' % info.save, '%s' % info.finalize
        )


def _addDescription( parameters, descriptions ):
    from ComponentInfo import Parameter
    ret = []
    for param in parameters:
        name = param.name
        d = descriptions.get( name ) or ''
        type = param.type
        value = param.value
        p = Parameter( name, type, value, d )
        ret.append( p )
        continue
    return ret
    

# version
__id__ = "$Id$"

# End of file 
