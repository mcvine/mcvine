#!/usr/bin/env python

from mccomponents.sample import matter

atoms = [matter.Atom('Cu', (0,0,0)), matter.Atom('Cu', (0.5, 0.5, 0)),
         matter.Atom('Cu', (0.5,0,0.5)), matter.Atom('Cu', (0, 0.5, 0.5))]
a=3.6149
alpha = 90.
lattice = matter.Lattice(a=a, b=a, c=a, alpha=alpha, beta=alpha, gamma=alpha)
fccCu = matter.Structure(atoms, lattice, sgid=225)

# End of file
