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

#include "mcstas2/mcstas2.h"

namespace mcstas2 {

    class E_monitor: public Component {
    public:
        E_monitor(const char * name,int in_nchan=20,char * in_filename="e.dat",double in_xmin=-0.2,double in_xmax=0.2,double in_ymin=-0.2,double in_ymax=0.2,double in_Emin=50,double in_Emax=60);
        ~E_monitor();
        void trace(double & x,double & y,double & z,double & vx,double & vy,double & vz,double & t,double & s1,double & s2,double & p);
    private:

            double *E_N, *E_p, *E_p2;
          
        int nchan;
        char * filename;
        double xmin;
        double xmax;
        double ymin;
        double ymax;
        double Emin;
        double Emax;
    }; // class E_monitor

} /* namespace mcstas2 */

// version
// $Id$

// Generated automatically by HHMill on Fri Jan 18 16:37:46 2008

// End of file 