// -*- C++ -*-
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//
//                                   Jiao Lin
//                      California Institute of Technology
//                        (C) 2007  All Rights Reserved
//
// {LicenseText}
//
// ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
//

#include "E_monitor.h"

namespace mcstas2 {

    E_monitor::E_monitor
    (const char * name,int in_nchan,char * in_filename,double in_xmin,double in_xmax,double in_ymin,double in_ymax,double in_Emin,double in_Emax)
    {
        setName( name );
        nchan = in_nchan;
        filename = in_filename;
        xmin = in_xmin;
        xmax = in_xmax;
        ymin = in_ymin;
        ymax = in_ymax;
        Emin = in_Emin;
        Emax = in_Emax;
        {
            int i;
            E_N = (double *)malloc(nchan*sizeof(double));
            E_p = (double *)malloc(nchan*sizeof(double));
            E_p2 = (double *)malloc(nchan*sizeof(double));

            for (i=0; i<nchan; i++)
            {
              E_N[i] = 0;
              E_p[i] = 0;
              E_p2[i] = 0;
            }
          }
    }


    E_monitor::~E_monitor
    ()
    {
        {
        #ifdef DEBUG
        printf("free: E_N = %p, E_p = %p, E_p2 = %p\n", E_N, E_p, E_p2);
        #endif
        free(E_N); free(E_p); free(E_p2);
        }
    }

    void
    E_monitor::trace
    (double & x,double & y,double & z,double & vx,double & vy,double & vz,double & t,double & s1,double & s2,double & p)
    {
        {
            int i;
            double E;

            PROP_Z0;
            if (x>xmin && x<xmax && y>ymin && y<ymax)
            {
              E = VS2E*(vx*vx + vy*vy + vz*vz);

              i = floor((E-Emin)*nchan/(Emax-Emin));
              if(i >= 0 && i < nchan)
              {
                E_N[i]++;
                E_p[i] += p;
                E_p2[i] += p*p;
                SCATTER;
              }
            }
          }
    }


} /* namespace mcstas2 */

// version
// $Id$

// Generated automatically by CCMill on Fri Jan 18 16:37:46 2008

// End of file 