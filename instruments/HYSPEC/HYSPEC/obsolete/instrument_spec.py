# this is obsolete. see HYSPEC/resources/hyspec_moderator2sample.instr

def computeOptions(
    Edes = None, E_min = None, E_max = None,
    toffset_us = -1.,
    freq = 180,
    LMS = 1.8,
    iv = -1.,
    LM3S = 0.72,
    Heusler = False, # Monochromator option
    ):
    "compute running options from input params"
    """Input parameters: 
      Incident energy - Edes (meV)
      Minimum and maximum energies - E_min, E_max (meV)
      Peak of time distribution, or if set to -1.0 a request for an estimate of optimal - toffset (s)
      Rotational frequency for fermi chopper T2 - freq (Hz)
      Monochromator to sample distance - LMS (m)
      Lattice spaceing for the monochromator - dPG (Angstrom)
      Gap between blades on the monochromator - m_gap (m)
      Horizontal mosaic on the monochromator - eta_h (arc minutes)
      Vertical mosaic on the monochromator - eta_v (arc minutes)
      Horizontal width of the monochromator blades - wid_h (m)
      Vertical width of the monochromator blades - wid_v (m)
      Number of blades along the horizontal for the monochromator - nos_h (#)
      Number of blades along the vertical for the monochromator - nos_v (#)
      Determines vertical focus of monochromator - iv 
      (selects 0=flat -1=focus at sample -2=focus at detector, or Radius in m when >0)
      Disc chopper T1A is in, logical - if_T1A (int, 0 or 1)
      Disc chopper T1B is in, logical - if_T1B (int, 0 or 1) 
      Fermi chopper T2 is in, logical - if_Fermi (int, 0 or 1)
      Generate event file just before monochromator, logical - out_PreMono (int, 0 or 1)
      Generate event file just outside of drum shield, logical - out_ExitDrum (int, 0 or 1)
      Generate event file at beamstop, logical - out_BeamStop (int, 0 or 1)
      Beam Stop is in, logical - if_BeamStop 
      Generate event file at sample position, logical - out_Sample  
      Generate event file at far field position, logical - out_FarField
    """

    """Distances:
      LMM - moderator to monochromator
      LCM - chopper to monochromator
      LMS - monochromator to sample
      LSD - sample to detector
      Radius of curvature Rc = (0.5*L2 + L3)*L2/x_mono
      where x_mono in the displacement of the monochromator
    """
    
    from math import sqrt, pi as PI, asin
    from mcni.utils.conversion import SE2V
    
    # /* Former parameters, now fixed */
    
    M4=3.0; # /* m value for G3 and all guides downstream - M4 () */
    Mi=2.0; # /* m value on the right side of the curved guide G2 - Mi () */
    LG4M=0.3; #/* Length between end of guide G4 and monochromator - LG4M (m) */
    ih=0.0; # /* Determines horizontal focus of monochromator - ih 
    # (selects 0=flat -1=focus at sample -2=focus at detector, or Radius in m when >0) */
    W0=0.04;# /* Width of guide at start of G3, assuming trumpet - W0 (m) */
    WS=0.0; #/* Effective width of guide at sample, assuming trumpet - WS (m) */
    H0=0.15; # /* Height of guide at start of G3, assuming trumpet - H0 (m) */
    HS=0.0; #/* Effective height of guide at sample, assuming trumpet - HS (m) */

    x_mono = 0.16 ;
    L1 = 9.93 ;
    L2 = 48. * 0.501 ;
    L3 = 5.0 ;
    Rc = (0.5*L2 + L3)*L2/x_mono ;
    LMM = L1 + L2 + L3 ;
    
    GAP_T0 = 0.23 + 0.07 ;        HALF_GAP_T0 = 0.5 * GAP_T0 ;
    GAP_T1A = 0.06 ;              HALF_GAP_T1A = 0.5 * GAP_T1A ;
    GAP_T1B = 0.06 ;              HALF_GAP_T1B = 0.5 * GAP_T1B ;
    GAP_T2 = 0.24 ;               HALF_GAP_T2 = 0.5 * GAP_T2 ;
    GAP_MON = 0.0456 ;            HALF_GAP_MON = 0.5 * GAP_MON ;
    GAP_VALV = 0.08 ;             HALF_GAP_VALV = 0.5 * GAP_VALV ;
    
    L_T2_M = 2.0098 ;
    L_T1B_M = 2.7854 ;
    L_MON1_M = 3.5664 ;
    L_MON2_M = 1.4774 ;
    L_VALV_M = 3.9106 ;
    L_SHUT2_M = 4.7370 ;
    
    POS_T0 = 8.50 ;
    POS_T1A = 9.40 ;
    
    POS_G1A = 2.3203 ;      LEN_G1A = 1.8686 ;
    POS_G1B = 4.2328 ;      LEN_G1B = 2.0875 ;
    POS_G1C = 6.3203 ;      LEN_G1C = POS_T0 - HALF_GAP_T0 - POS_G1C ;
    POS_T0_T1A = POS_T0 + HALF_GAP_T0 ;
    LEN_T0_T1A = POS_T1A - POS_T0 - HALF_GAP_T1A - HALF_GAP_T0 ;
    POS_T1A_G2 = POS_T1A + HALF_GAP_T1A ;
    LEN_T1A_G2 = L1 - POS_T1A_G2 ;
    
    POS_G3 = LMM - L3 + 0.001 ;       POS_SHUT2 = LMM - L_SHUT2_M ;
    LEN_G3 = POS_SHUT2 - POS_G3 ;     LEN_SHUT2 = 0.5 ; 
    POS_VALV = LMM - L_VALV_M ;
    LEN_SHUT2_VALV = POS_VALV - POS_SHUT2 - HALF_GAP_VALV - LEN_SHUT2 ;
    POS_MON1 = LMM - L_MON1_M ;
    LEN_VALV_MON1 = POS_MON1 - POS_VALV - HALF_GAP_VALV - HALF_GAP_MON ;
    POS_T1B = LMM - L_T1B_M ;
    LEN_MON1_T1B = POS_T1B - POS_MON1 - HALF_GAP_MON - HALF_GAP_T1B ;
    POS_T2 = LMM - L_T2_M ;
    LEN_T1B_T2 = POS_T2 - POS_T1B - HALF_GAP_T1B - HALF_GAP_T2 ;
    POS_MON2 = LMM - L_MON2_M ;
    LEN_T2_MON2 = POS_MON2 - POS_T2 - HALF_GAP_T2 - HALF_GAP_MON ;
    POS_G4 = POS_MON2 + HALF_GAP_MON ;
    LEN_G4 = LMM - POS_G4 - LG4M ; 
    if (LEN_G4 <= 0.0) : LEN_G4 = 0.001 
    WA = W0 + WS * POS_G3 / (LMM + LMS - POS_G3) ; WB = WS / (LMM + LMS - POS_G3) ;
    HA = H0 + HS * POS_G3 / (LMM + LMS - POS_G3) ; HB = HS / (LMM + LMS - POS_G3) ;

    W1_G3 = WA ; W2_G3 = WA - WB * (POS_G3 + LEN_G3) ;
    H1_G3 = HA ; H2_G3 = HA - HB * (POS_G3 + LEN_G3) ;
    W1_SHUT2 = WA - WB * POS_SHUT2 ; W2_SHUT2 = WA - WB * (POS_SHUT2 + LEN_SHUT2) ;
    H1_SHUT2 = HA - HB * POS_SHUT2 ; H2_SHUT2 = HA - HB * (POS_SHUT2 + LEN_SHUT2) ;
    W1_SHUT2_VALV = WA - WB * (POS_SHUT2 + LEN_SHUT2) ; 
    W2_SHUT2_VALV = WA - WB * (POS_SHUT2 + LEN_SHUT2 + LEN_SHUT2_VALV) ;
    H1_SHUT2_VALV = HA - HB * (POS_SHUT2 + LEN_SHUT2) ; 
    H2_SHUT2_VALV = HA - HB * (POS_SHUT2 + LEN_SHUT2 + LEN_SHUT2_VALV) ;
    W1_VALV_MON1 = WA - WB * (POS_VALV + HALF_GAP_VALV) ; 
    W2_VALV_MON1 = WA - WB * (POS_VALV + HALF_GAP_VALV + LEN_VALV_MON1) ;
    H1_VALV_MON1 = HA - HB * (POS_VALV + HALF_GAP_VALV) ; 
    H2_VALV_MON1 = HA - HB * (POS_VALV + HALF_GAP_VALV + LEN_VALV_MON1) ;
    W1_MON1_T1B = WA - WB * (POS_MON1 + HALF_GAP_MON) ; 
    W2_MON1_T1B = WA - WB * (POS_MON1 + HALF_GAP_MON + LEN_MON1_T1B) ;
    H1_MON1_T1B = HA - HB * (POS_MON1 + HALF_GAP_MON) ; 
    H2_MON1_T1B = HA - HB * (POS_MON1 + HALF_GAP_MON + LEN_MON1_T1B) ;
    W1_T1B_T2 = WA - WB * (POS_T1B + HALF_GAP_T1B) ; 
    W2_T1B_T2 = WA - WB * (POS_T1B + HALF_GAP_T1B + LEN_T1B_T2) ;
    H1_T1B_T2 = HA - HB * (POS_T1B + HALF_GAP_T1B) ; 
    H2_T1B_T2 = HA - HB * (POS_T1B + HALF_GAP_T1B + LEN_T1B_T2) ;
    W1_T2_MON2 = WA - WB * (POS_T2 + HALF_GAP_T2) ; 
    W2_T2_MON2 = WA - WB * (POS_T2 + HALF_GAP_T2 + LEN_T2_MON2) ;
    H1_T2_MON2 = HA - HB * (POS_T2 + HALF_GAP_T2) ; 
    H2_T2_MON2 = HA - HB * (POS_T2 + HALF_GAP_T2 + LEN_T2_MON2) ;
    W1_G4 = WA - WB * POS_G4 ; W2_G4 = WA - WB * (POS_G4 + LEN_G4) ;
    H1_G4 = HA - HB * POS_G4 ; H2_G4 = HA - HB * (POS_G4 + LEN_G4) ;
    
    LSD = 4.5 ;
    
    """
    if ( if_Ortho30 > 0.9 && if_Ortho30 < 1.1 ):
        sourcename= "/SNS/users/2xy/HYSPEC_model/source/SNS_TD_30o70p_fit_fit.dat"
    else:
        sourcename= "/SNS/users/2xy/HYSPEC_model/source/SNS_TD_0o100p_fit_fit.dat"
        pass
    """
    # /* Determine whether an estimate of toffset is requested, then make the estimate */

    if (toffset_us > -1.1 and toffset_us < -0.9):
        toffset_s = 0.3 * pow(( 1.0 + Edes ),(-0.9)) / 1000.0 
    else:
        toffset_s = toffset_us / 1000000.0 
        pass
    
    if (Edes < 60.0) :
        freq_T0 = 30.0; 
    else:
        freq_T0 = 60.0;
        pass
    
    # /* Calculate the phase of the disc choppers or the time width at the TOF monitors*/
    # /* calculate the number of energy bins for the energy monitors */
    nos_eng = E_max - E_min ;
    if( nos_eng < 6 ): nos_eng = 100 
    
    # /* calculate T0 chopper phase */
    phase_0 = POS_T0/(sqrt(Edes)*SE2V)+toffset_s;
    
    # /* calculate T1A chopper phase */
    phase_1A = POS_T1A/(sqrt(Edes)*SE2V)+toffset_s;
    t_T1A_min = POS_T1A/(sqrt(E_max)*SE2V) - 0.0020 + toffset_s;
    t_T1A_max = POS_T1A/(sqrt(E_min)*SE2V) + 0.0020 + toffset_s;
    ang_freq_1A = 2.0*PI*60.0 ;
    radius_1A = 0.250 ;
    wid_1A = 0.0946 ;
    nos_t1a = 100000. * (t_T1A_max - t_T1A_min) ;
    
    # /* The T1B chopper parameters */
    phase_1B = POS_T1B/(sqrt(Edes)*SE2V)+toffset_s;
    t_T1B_min = POS_T1B/(sqrt(E_max)*SE2V) - 0.0020 + toffset_s;
    t_T1B_max = POS_T1B/(sqrt(E_min)*SE2V) + 0.0020 + toffset_s;
    ang_freq_1B = 2.0*PI*60.0 ;
    radius_1B = 0.250 ;
    wid_1B = 0.0946 ;
    nos_t1b = 100000. * (t_T1B_max - t_T1B_min) ;
    
    """/* The T2 FermiChopper parameters:
    dist_eff - The routine uses distance & nominal velocity to set the phase angle
    vi_eff   - and we therefore have to calculate an effective distance to account
             - for the offset time. 
    """
    len = 0.01 ;   #   /* length of chopper slit */
    wid = 0.0006  ; #  /* width of one chopper slit */    
    nos = 77 ;     #  /* number of chopper slits; note actual number is 64, but since we ignore Gd blade 0.6 mm thick... */
    trn = 1.0  ;    #  /* transmission; account for Gd blade and E-dependent Al transmission AFTER results */
    barrel = 0.12 ;       
    height = 0.155 ;
    vi_eff = sqrt(Edes) * SE2V ;
    dist_eff = POS_T2 + vi_eff * toffset_s ;
    t_T2_min = (POS_T2 + HALF_GAP_T2 - 0.0004)/(sqrt(Edes)*SE2V) - 0.000125 + toffset_s;    
    t_T2_max = (POS_T2 + HALF_GAP_T2 - 0.0004)/(sqrt(Edes)*SE2V) + 0.000125 + toffset_s;
    b_radius = barrel / 2.0 ;
    b_height_min = -height / 2.0 ;
    b_height_max =  height / 2.0 ;
    nos_t2 = 100000. * (t_T2_max - t_T2_min) ;
    
    # /* Flight times at the end of the curved guide G2 */
    t2_min = (L1 + L2)/(sqrt(E_max)*SE2V) - 0.0020 + toffset_s;    
    t2_max = (L1 + L2)/(sqrt(E_min)*SE2V) + 0.0020 + toffset_s;    
    nos_g2 = 100000. * (t2_max - t2_min) ;
    
    # /* Flight times at monitor 0 */
    t_mon0_min = POS_G1A /(sqrt(E_max)*SE2V) - 0.0020 + toffset_s ;    
    t_mon0_max = POS_G1A /(sqrt(E_min)*SE2V) + 0.0020 + toffset_s ;    
    nos_mon0 = 100000. * (t_mon0_max - t_mon0_min) ;
    
    # /* Flight times at monitor 1 */
    t_mon1_min = POS_MON1/(sqrt(E_max)*SE2V) - 0.0020 + toffset_s;    
    t_mon1_max = POS_MON1/(sqrt(E_min)*SE2V) + 0.0020 + toffset_s;    
    nos_mon1 = 100000. * (t_mon1_max - t_mon1_min) ;
    
    # /* Flight times at monitor 2 */
    t_mon2_min = POS_MON2/(sqrt(Edes)*SE2V) - 0.000125 + toffset_s;    
    t_mon2_max = POS_MON2/(sqrt(Edes)*SE2V) + 0.000125 + toffset_s;    
    nos_mon2 = 100000. * (t_mon2_max - t_mon2_min) ;
    
    # /* Flight times at the end of the final guide G4 */
    t4_min = (POS_G4 + LEN_G4)/(sqrt(Edes)*SE2V) - 0.000125 + toffset_s;    
    t4_max = (POS_G4 + LEN_G4)/(sqrt(Edes)*SE2V) + 0.000125 + toffset_s;
    nos_g4 = 100000. * (t4_max - t4_min) ;

    # /* Flight times at monitor 3 */
    t_mon3_min =(LMM + LMS - LM3S) /(sqrt(Edes)*SE2V) - 0.000125 + toffset_s;    
    t_mon3_max =(LMM + LMS -LM3S)/(sqrt(Edes)*SE2V) + 0.000125 + toffset_s;    
    nos_mon3 = 100000. * (t_mon3_max - t_mon3_min) ;
    
    # /* Flight times at the sample and detector */
    phasefs_min = (LMM + LMS)/(sqrt(Edes)*SE2V) - 0.0002 + toffset_s ;
    phasefs_max = (LMM + LMS)/(sqrt(Edes)*SE2V) + 0.0002 + toffset_s ;
    nos_samp = 100000. * (phasefs_max - phasefs_min) ;
    phaseff_min = (LMM + LMS + LSD)/(sqrt(Edes)*SE2V) - 0.0002 + toffset_s ;
    phaseff_max = (LMM + LMS + LSD)/(sqrt(Edes)*SE2V) + 0.0002 + toffset_s ;
    nos_det = 100000. * (phaseff_max - phaseff_min) ;
    
    # /* consider replacing dPG, m_gap, eta_h, eta_v, wid_h, wid_v, nos_h, nos_v ALL with if_Heusler */

    if not Heusler:
        dPG = 3.3539 ;
        m_gap = 0.0014 ;# /* A GUESS.  STILL NEEDS TO BE MEASURED */
        eta_h = 72.0 ; #  /* From 1.2 deg FWHM, MH email Dec 6, 2011 */
        eta_v = 72.0 ; # /* From 1.2 deg FWHM, MH email Dec 6, 2011 */
        wid_h = 0.3 ;
        wid_v = 0.012 ;
        nos_h = 1.0 ;
        nos_v = 13.0 ;
    else :
        dPG = 3.43 ;
        m_gap = 0.00125 # /* A GUESS.  STILL NEEDS TO BE MEASURED */
        eta_h = 48.0 * 0.45 / 0.8 ;
        eta_v = 48.0 * 0.45 / 0.8 ; 
        wid_h = 0.15 ;
        wid_v = 0.015 ;
        nos_h = 1.0 ;
        nos_v = 9.0 ;
        pass
    
    # /* Calculate the monochromator parameter values */
    WL_mean = sqrt(81.81/Edes);
    Q_m = 2.0*PI/dPG ;
    k_m = 2.0*PI/WL_mean ;
    sin_tm = Q_m / (2.0 * k_m) ;
    Cl_ang = asin(sin_tm) * 180.0/PI ;
    Al_ang = 2.0 * Cl_ang ;
    if(iv < -0.1) :
        L1V = LMM ; L2V = LMS ;
        if(iv > -1.5 and iv < -0.5): L2V = LMS ;
        if(iv > -2.5 and iv < -1.5): L2V = LMS + LSD ;
        R_vert = 2.0 * L1V * L2V * sin_tm / (L1V + L2V) ; 
        pass
    if(iv > -0.1 and iv < 0.1): R_vert = 10000.0
    if(iv > 0.1) : R_vert = iv 
    R_horz = 10000.0 ; 
    
    components = [
        ('moderator',  
         dict(
             Emin = E_min,
             Emax = E_max,
             ),
         )
        ('mon0_tof',
         dict(
            tmin = t_mon0_min,
            tmax = t_mon0_min,
            z = POS_G1A-0.002,
            ),
        mon0_total = dict(
            z = POS_G1A-0.001,
            )
        g1a_guide = dict(
            l = LEN_G1A,
            z = POS_G1A,
            )
        g1b_guide = dict(
            l = LEN_G1B,
            z = POS_G1B,
            )
        g1c_guide = dict(
            l = LEN_G1C,
            z = POS_G1C,
            )
        
    return


