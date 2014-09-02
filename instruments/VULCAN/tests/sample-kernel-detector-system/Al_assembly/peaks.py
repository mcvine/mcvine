from mccomponents.sample.diffraction.SimplePowderDiffractionKernel import Peak

# q=(2*pi/a)*sqrt(h^2+k^2+l^2) - Qvector

peaks = [
    Peak(q=2.69, F_squared=1.69, multiplicity=8, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(q=3.10, F_squared=1.69, multiplicity=6, intrinsic_line_width=0, DebyeWaller_factor=0),
    ]

# added to include data regarding volume and cross sections
# unit: \AA
a = 4.049320
unitcell_volume = a**3

natoms = 4

# unit: barns
class cross_sections:
    coh = natoms * 1.495
    inc = natoms * 0.0082
    abs = natoms * 0.231


