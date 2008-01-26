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



formatstr = '''
Compoennt %(name)r: %(simple_description)s

%(full_description)s
'''

class ComponentInfo:

    def __init__(self, name = 'name', copyright = '', simple_description ='',
                 full_description = '', 
                 definition_parameters = [],
                 setting_parameters = [],
                 output_parameters = [],
                 state_parameters = [],
                 declare = '',
                 initialize='', trace='', save='', finalize=''
                 ):
        self.name = name
        self.copyright = copyright
        self.simple_description =simple_description
        self.full_description = full_description
        self.definition_parameters = definition_parameters
        self.setting_parameters = setting_parameters
        self.output_parameters = output_parameters
        self.state_parameters = state_parameters
        self.declare = declare
        self.initialize = initialize
        self.trace = trace
        self.save = save
        self.finalize = finalize
        return

    def __str__(self):
        d = self.__dict__
        return formatstr % d

    pass # end of ComponentInfo


value_converters = {
    'float': float,
    'double': float,
    'int': int,
    'char *': str,
    }


class Parameter:

    def __init__(self, name='name', type='', value='', description = '' ):
        self.name = '%s' % name
        type = '%s' % type
        
        #string --> char *
        if type == 'string': type = 'char *'
        #default type is double
        if type == '': type = 'double'
        
        self.type = type

        value_converter = value_converters[type]
        try:
            value = value_converter( value )
        except:
            value = value_converter( )
        self.value = value
        
        self.description = '%s' % description
        return

    def __str__(self):
        return '%s(%s, default = %s): %s' % (
            self.name, self.type, self.value, self.description)


    __repr__ = __str__
    
    pass # end of Parameter

# version
__id__ = "$Id$"

# End of file 
