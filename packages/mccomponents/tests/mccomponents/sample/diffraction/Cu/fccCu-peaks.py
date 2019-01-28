from mccomponents.sample.diffraction.SimplePowderDiffractionKernel import Peak

peaks = [
    Peak(hkl=(1, 1, 1), d=2.0870634880935786, q=3.010538655399958, F=(30.03723137474607-5.517749888749685e-15j), F_squared=9.022352686600298, multiplicity=8, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(0, 0, 2), d=1.8074500000000002, q=3.476270606201879, F=(29.764021621217278-3.645041380817636e-15j), F_squared=8.858969830682897, multiplicity=6, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(0, 2, 2), d=1.2780601516556254, q=4.916189037769638, F=(28.695807951162525-7.02844587126767e-15j), F_squared=8.234493939700023, multiplicity=12, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(1, 1, 3), d=1.0899333595141578, q=5.764742635256472, F=(27.919882836043882-8.547998786932568e-15j), F_squared=7.795198575784179, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(2, 2, 2), d=1.0435317440467893, q=6.021077310799916, F=(27.66593185723957-1.016429846831917e-14j), F_squared=7.654037855294233, multiplicity=8, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(0, 0, 4), d=0.9037250000000001, q=6.952541212403758, F=(26.673017425822827-6.5330050828271e-15j), F_squared=7.114498585982481, multiplicity=6, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(1, 3, 3), d=0.8293149363686938, q=7.5763561364174326, F=(25.951787894599445-1.1123620892045283e-14j), F_squared=6.734952949262782, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(0, 2, 4), d=0.808316213186399, q=7.773177383651803, F=(25.71573812403783-9.447808914394345e-15j), F_squared=6.612991872640928, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(2, 2, 4), d=0.7378883725989094, q=8.515089193030164, F=(24.79281502751436-1.2144976626119145e-14j), F_squared=6.14683676988542, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(1, 1, 5), d=0.6956878293645262, q=9.031615966199873, F=(24.122425544594787-1.0339507930800423e-14j), F_squared=5.818914141545191, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(3, 3, 3), d=0.6956878293645261, q=9.031615966199873, F=(24.122425544594783-1.3293653053886255e-14j), F_squared=5.818914141545189, multiplicity=8, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(0, 4, 4), d=0.6390300758278127, q=9.832378075539276, F=(23.04514960476316-1.1288867479738039e-14j), F_squared=5.310789203059156, multiplicity=12, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(1, 3, 5), d=0.611029623083623, q=10.28294712696719, F=(22.422016414353102-1.2356572784520123e-14j), F_squared=5.0274682008552, multiplicity=48, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(2, 4, 4), d=0.6024833333333334, q=10.428811818605636, F=(22.21807239894913-1.3604645623298603e-14j), F_squared=4.9364274112494515, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(3, 3, 5), d=0.5512670818953327, q=11.397715397003434, F=(20.841470487953178-1.4037892067427735e-14j), F_squared=4.343668921002233, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(4, 4, 4), d=0.5217658720233946, q=12.042154621599831, F=(19.910717704992937-1.4630158023687682e-14j), F_squared=3.964366795279192, multiplicity=8, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(1, 5, 5), d=0.5061872475752853, q=12.412768866218991, F=(19.37233851198905-1.3048349792888513e-14j), F_squared=3.7528749942309414, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(3, 5, 5), d=0.4706198943045803, q=13.350870592634095, F=(18.00676682770625-1.433375408305308e-14j), F_squared=3.2424365158738224, multiplicity=24, intrinsic_line_width=0, DebyeWaller_factor=0),
    Peak(hkl=(5, 5, 5), d=0.4174126976187157, q=15.052693276999786, F=(15.557618728237149-1.4289440983417905e-14j), F_squared=2.4203950049319527, multiplicity=8, intrinsic_line_width=0, DebyeWaller_factor=0)
    ]

# unit: \AA
unitcell_volume = 47.2377130159

# unit: barns
class cross_sections:
    coh = 0
    inc = 0
    abs = 15.12
