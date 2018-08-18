from mccomponents.sample.diffraction.SimplePowderDiffractionKernel import Peak

peaks = [
    Peak(q=1.9200, F_squared=0.0, multiplicity=12, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(q=3.1353, F_squared=3.3, multiplicity=8, intrinsic_line_width=0, DebyeWaller_factor=0),
    ]

# unit: \AA
a = 4.049320
unitcell_volume = a**3

natoms = 4

# unit: barns
class cross_sections:
    coh = natoms * 1.495
    inc = natoms * 0.0082
    abs = natoms * 0.231

