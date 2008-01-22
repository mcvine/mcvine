#!/usr/bin/env python
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                        (C) 2005 All Rights Reserved  
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#




def component2HHandCC( component_filename, pathToSave ):
    from mcstas2.utils.mills.cxx.factory import createHHandCC
    return createHHandCC( component2cppClass( component_filename ), pathToSave )




def component2cppClass( comp_filename ):
    #parse the mcstas component and get infos we want
    from mcstas2.utils.parsers import parseComponent
    compInfo = parseComponent( comp_filename )

    #massage those info and add some additional info and make the class
    class_name = compInfo.name
    ctor_args = _arguments(compInfo.definition_parameters) \
                + _arguments(compInfo.setting_parameters)
    output_params = compInfo.output_parameters
    trace_method_args = compInfo.state_parameters
    private_member_declaration = compInfo.declare[1:-1]
    ctor_body = compInfo.initialize
    trace_method_body = compInfo.trace
    save_method_body = compInfo.save
    finalize_body = compInfo.finalize

    ##     print class_name
    ##     for arg in ctor_args: print arg
    ##     print private_member_declaration
    ##     print ctor_body
    ##     print finalize_body

    ##     print compInfo.header
    ##     print compInfo.save
    namespace = "mcstas2"
    baseclass = Class( 'Component' )
    headers_dependent_on = ['mcstas2/mcstas2.h']
    return createCppClass( class_name,
                           namespace, baseclass,
                           ctor_args, ctor_body,
                           private_member_declaration,
                           trace_method_args,
                           trace_method_body,
                           save_method_body,
                           finalize_body,
                           headers_dependent_on)


from mcstas2.utils.mills.cxx.Class import Argument, Method, Member, Class, argument2Member

def createCppClass( name,
                    namespace, baseclass,
                    ctor_args, ctor_body,
                    private_member_declaration,
                    trace_method_args,
                    trace_method_body,
                    save_method_body,
                    finalize_body,
                    headers_dependent_on):

    #ctor arguments become private members.
    # E_monitor( int nchan ) --> E_mointor( int in_nchan ) { nchan = in_nchan; }
    #
    private_members = [ argument2Member(arg) for arg in ctor_args ]

    # meta-methods
    ctor_args_name = Argument( 'const char *', 'name' )
    ctor_body_name = 'setName( name );'
    
    #   other ctor arguments all will have prefix 'in_'
    ctor_args = [
        Argument( arg.type,  "%s" % arg.name, arg.default ) for arg in ctor_args ]
    #
    #   transfer inputs to private members
    ctor_getInputs = [ "this->%s = %s;" % (member.name, arg.name) for member, arg in \
                       zip( private_members, ctor_args ) ]
    #   ctor body
    ctor_body = ctor_body.split("\n")
    ctor_body = [ctor_body_name] + ctor_getInputs + ctor_body

    ctor_args = [ ctor_args_name ] + ctor_args
    ctor = Method( name, ctor_args, ctor_body )

    # dtor
    dtor = Method( '~'+name, [], ['save();', 'finalize();'] )
    
    #   finalize
    finalize = Method( 'finalize', [], finalize_body.split("\n"), type = 'void' )

    # methods
    trace_body = trace_method_body.split('\n')
    trace_arguments = [ Argument( "double &", arg ) for arg in trace_method_args ]
    trace = Method( "trace", trace_arguments, trace_body, type = "void" )

    save_body = save_method_body.split( '\n' )
    save_body = [ 'mcuse_format("McStas");' ] + save_body # need to call mcuse_format before calling detector output methods
    save = Method( 'save', [], save_body, type = 'void' )
    
    methods = [ctor, dtor, trace, save, finalize, ]

    # data
    private = private_member_declaration.split("\n")

    # the class
    klass = Class(
        name,
        namespace = namespace,
        parents = [ baseclass ],
        public_methods = methods, private = private,
        private_members = private_members,
        headers_dependent_on = headers_dependent_on,
        )
    
    return klass



def _argument( param ):
    """Create an argument.
    input: parsed mcstas parameter. 
    note: mcstas parameters without type are doubles
    """
    if param.type == "": return Argument("double", param.name, param.value)
    return Argument( param.type, param.name, param.value )


def _arguments( params ):
    if params == "": return []
    return [ _argument(param) for param in params ]



# version
__id__ = "$Id$"

# End of file 
