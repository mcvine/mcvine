

textMain = """
/* Here, a secondary arm - or reference point, placed  */
/* on the sample position. The ROT parameter above     */

COMPONENT L_monitor9 = L_monitor(
    nchan = 140, filename = "Vulcan_asbuilt_L_monitor9.txt",
    xwidth = 0.15, yheight = 0.15, Lmin = 0.0, Lmax = 14.0,
    restore_neutron = 1)
  AT (0, 0, 0.971)  RELATIVE  FU_Out
  ROTATED (0,ROT,0) relative arm

COMPONENT arm2 = Arm()
  AT (0,0,0) RELATIVE target
  ROTATED (0,ROT,0) relative arm

FINALLY
%{
%}
/* The END token marks the instrument definition end */
END


  """

textExample = """COMPONENT L_monitor9 = L_monitor(
    nchan = 140, filename = "Vulcan_asbuilt_L_monitor9.txt",
    xwidth = 0.15, yheight = 0.15, Lmin = 0.0, Lmax = 14.0,
    restore_neutron = 1)
  AT (0, 0, 0.971)  RELATIVE  FU_Out
  ROTATED (0,ROT,0) relative arm
"""

# Parameter "options" has equal character ('=')
textOptions = """COMPONENT psd_yscan_L = Monitor_nD(
    options = "square, wavelength limits=[0.875 3.025] bins=21 y limits=[-0.05 0.05] bins=100, file=Vulcan_asbuilt_yscan.txt",
    xwidth = 0.1, yheight = 0.1)
  AT (0, 0, 0.975) RELATIVE FU_Out

"""

