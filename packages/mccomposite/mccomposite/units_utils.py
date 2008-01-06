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


class UnitsRemover:

    '''to remove units from inputs.

    To render a computation engine of a python representation, the units
    attached to the python representation tree need to be removed because
    the computation engine (c++) is usually fixed 
    '''

    categories = [
        'length',
        'angle',
        ]
    
    def __init__(self, **kwds):
        '''create a new units remover
 Examples:
    UnitsRemover( length_unit = meter, angle_unit = degree, ... )
    '''
        post = '_unit'
        for k,v in kwds.iteritems():
            assert k.endswith( post )
            category = k[:-len(post)]
            assert category in self.categories
            setattr(self, k, v)
            continue
        return


    def remove_length_unit( self, something ):
        return remove_unit( something, self.length_unit )
        
    def remove_angle_unit( self, something ):
        return remove_unit( something, self.angle_unit )
        
    pass # end of UnitsRemover


def remove_unit( something, unit ):
    '''remove unit from a scalar or a vector
  Parameters:
    something: a scalar or a vector
    unit: the unit to be removed

  Examples
    remove_unit( 1*meter, meter ) --> 1
    remove_unit( (1*meter, 2*meter), meter ) --> (1,2)
    remove_unit( (1*meter, 1*cm), meter ) --> (1,0.01)
    '''
    if '__iter__' in dir(something):
        if not is_unitless_vector( something ):
            return remove_unit_of_vector( something, unit)
    else:
        if not is_unitless_scalar( something ):
            return remove_unit_of_scalar( something, unit )
        pass
    return something




def is_unitless_scalar( s ):
    return isinstance(s, float) or isinstance(s, int)

def remove_unit_of_scalar( s, unit ):
    try:
        s+unit
        return s/unit
    except:
        raise ValueError, "incommpatible unit: %s, %s" % (s, unit)
    

def is_unitless_vector( v ):
    for i in v:
        if not is_unitless_scalar( i ):
            return False
        continue
    return True


def remove_unit_of_vector( v, unit ):
    from numpy import array
        
    v = array(v) * 1.0
    try:
        v[0] + unit
        #this means the v has compatible unit
        v = v/unit
    except:
        pass

    for i in v:
        if not isinstance(i, float):
            raise ValueError , "v should have unit of length: %s" %(
                v, )
        continue
    # this means v already is a unitless vector
    return v



# version
__id__ = "$Id$"

# End of file 
