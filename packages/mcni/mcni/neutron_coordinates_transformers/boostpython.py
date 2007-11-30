from mcni import mcnibp as binding


def applyOffsetRotation(offset, rotation, neutrons):
    r = binding.Position_double(*offset)
    rotmat = rotation.copy()
    rotmat.shape = -1,
    m = binding.RotationMatrix_double( *rotmat )
    binding.abs2rel_batch( neutrons, r, m )
    return

