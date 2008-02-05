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


## Parsers to parse Riseo McStas files such as
##  - McStas component file


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

    from ComponentInfo import Parameter
    name_parameter = Parameter( 'name', 'char *', name.lower(), 'component name' )
    input_parameters = [name_parameter] + definition_parameters + setting_parameters
    
    output_parameters = _addDescription( info.output_parameters, outputParamDescs )

    state_parameters = [ str(p) for p in info.state_parameters ]

    # the original McStas component does not need a "name" argument, but
    # the auto-generated c++ class and python component need a "name"
    # argument. So we better add this to the description, which will
    # become the documentation.
    full_description = header.full_description.replace(
        name+'(', name+'(name, ')
    
    from ComponentInfo import ComponentInfo
    return ComponentInfo(
        name,
        header.copyright, header.simple_description,
        full_description,
        input_parameters,
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
