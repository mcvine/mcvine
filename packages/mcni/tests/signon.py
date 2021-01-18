#!/usr/bin/env python
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 
#                               Michael A.G. Aivazis
#                        California Institute of Technology
#                        (C) 1998-2005  All Rights Reserved
# 
#  <LicenseText>
# 
#  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 

if __name__ == "__main__":

    import mcni
    from mcni import mcni as mcnimodule

    print("copyright information:")
    print("   ", mcni.copyright())
    print("   ", mcnimodule.copyright())

    print()
    print("module information:")
    print("    file:", mcnimodule.__file__)
    print("    doc:", mcnimodule.__doc__)
    print("    contents:", dir(mcnimodule))

    print()
    print(mcnimodule.hello())

# version
__id__ = "$Id$"

#  End of file 
