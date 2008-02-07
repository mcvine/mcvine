
filetype = 'Neutron'

#number of doubles per neutron
ndblsperneutron = 10

#number of bytes per double
nbytesperdbl = 8

#number of chars for entries in the neutron data file
titlesize = 64
versionsize = 4
commentsize = 1024
nsize = 8
neutronsize = ndblsperneutron * nbytesperdbl


#version
version = 1



# packing and unpacking related stuff
from struct import calcsize
intSize = calcsize('<i')
assert intSize == versionsize
longlongsize = calcsize('<q')
assert longlongsize == nsize
dubSize = calcsize('<d')
assert dubSize == nbytesperdbl
strSize = calcsize('<s')
assert strSize == 1


headerfmtstr = '<%(titlesize)dsi%(commentsize)dsq' % {
    'titlesize': titlesize,
    'commentsize': commentsize,
    }
headersize = calcsize( headerfmtstr )

neutronsfmtstr = '<%id'

def filesize( n ):
    '''calculate neutron file size given number of neutrons
    '''
    return headersize + calcsize( neutronsfmtstr % (n*ndblsperneutron) )
