# -*- Python -*-

"""
Debye temperature of elements
"""

def getT(element, default=None):
    return table.get(element, default)


table = dict(
    Li=344, Be=1440, C=2230, Ne=75,
    Na=158, Mg=400, Al=428, Si=645, Ar=92,
    K=91, Ca=230, Sc=360, Ti=420, V=380, Cr=630, Mn=410, Fe=470, Co=445, Ni=450, Cu=343, Zn=327, Ga=320, Ge=374, As=282, Se=90, Kr=72,
    Rb=56, Sr=147, Y=280, Zr=291, Nb=275, Mo=450, Ru=600, Rh=480, Pd=274, Ag=225, Cd=209, In=108, Sn=200, Sb=211, Te=153, Xe=64,
    Cs=38, Ba=110, La=142, Hf=252, Ta=240, W=400, Re=430, Os=500, Ir=420, Pt=240, Au=165, Hg=71.9, Tl=78.5, Pb=105, Bi=119, 
    Gd=200, Dy=210, Yb=120, Lu=210,
    Th=163, U=207, 
    )

# End of file
