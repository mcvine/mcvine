#ifndef SNS_SOURCE_LIB_H
#define SNS_SOURCE_LIB_H

#include <cmath>
#include <string.h>
#include <functional>

namespace mcstas2 { namespace SNSsource {
  // functor
  struct F1: public std::unary_function<double, double> {
    virtual double operator()(double) const = 0;
    virtual ~F1() {}
  };
  struct F2: public std::binary_function<double, double, double> {
    virtual double operator()(double, double) const = 0;
    virtual ~F2() {}
  };

#define Maxlength 200
#define MAXCOLS 500
  /* ----------------------------------------------------------------
     routine to load E, I and t I data from SNS source files
     -----------------------------------------------------------------*/
  void sns_source_load(char filename[], double *xvec, double *yvec, int xcol, int ycol, int *veclenptr, double *tcol, double *Ecol, double **Imat,int *ntvals, int *nEvals);

  /*----------------------------------------------------------------------
    routine to do a 1D linear interpolation
    ------------------------------------------------------------------------*/
  /* given a point (x1,y1) on the low side of xdes and one (x2,y2) on the
     high side of xdes return the interpolated y values */
  double linint(double xdes,double x1, double x2, double y1, double y2);
  double linfuncint(double xdes, double xylen, double *vecx, double *vecy);

  /*------------------------------------------------------------------------
    routine to perform a 1 d quadratic interpolation 
    --------------------------------------------------------------------------*/
  /* given 2 points on the low side of xdes and one on the high side, return
     a quadratically interpolated result */
  double quadint(double xdes,double x1, double x2,double x3, double y1, double
                 y2, double y3);
  double quadfuncint(double xdes, double xylen, double *vecx, double *vecy);

  /*-------------------------------------------------------------------
    integration routines
    ---------------------------------------------------------------------*/
  double integtrap(const F1 &,double prev,double low,double high, int step);
  double integ1(const F1 &,double low, double high, double err);

  /*---------------------------------------------------------------------------
    Routine for finding zeros. 
    Modified version of rtbis from "Numerical Recipes in C: pg 354
    -----------------------------------------------------------------------------*/
  double zero_find(const F2 &,double yval,double xmin,double xmax, double tol);

  /*----------------------------------------------------------------------------
    Routine for calculating Probability distribution
    ----------------------------------------------------------------------------*/
  void Pcalc(const F1 &,double llim, double hlim, double *xvec, double *Prob, int veclen, int *idxstart, int *idxstop);

  /*----------------------------------------------------------------------------
    Routine for calculating t Probability distribution
    ----------------------------------------------------------------------------*/
  void tPcalc(const F1 &,double llim, double hlim, double *xvec, double *Prob, int veclen, int *idxstart, int *idxstop);

  // use macros to replace the following functions
  /*-----------------------------------------------------------------
    Functions for random energy generation
    ------------------------------------------------------------------*/
  /*
    double xonly(double x)
    {
    return linfuncint(x,xylength,inxvec,inyvec);
    }
  */
  struct Xonly: public F1 {
    Xonly( double xylength, double * inxvec, double * inyvec ) 
      : m_xylength( xylength ),
        m_inxvec( inxvec ),
        m_inyvec( inyvec )
    {}
    double operator() ( double x ) const 
    { return linfuncint(x, m_xylength, m_inxvec, m_inyvec ); }
    double m_xylength, *m_inxvec, *m_inyvec;
  };
  /*
    double Pfunc(double x, double y)
    {
    return quadfuncint(x,xylength,inxvec,Pvec)-y;
    }
  */
  struct Pfunc: public F2 {
    Pfunc( double xylength, double *inxvec, double *Pvec)
      : m_xylength( xylength ),
        m_inxvec( inxvec ),
        m_Pvec( Pvec )
    {}
    double operator() (double x, double y) const 
    { return quadfuncint(x, m_xylength, m_inxvec, m_Pvec)-y; }
    double m_xylength, *m_inxvec, *m_Pvec;
  };
  /*----------------------------------------------------------------
    Functions for random time generation
    ------------------------------------------------------------------*/
  /*
    double txonly(double t)
    {
    return linfuncint(t,ntvals,txval,tyval);
    }
  */
  struct Txonly: public F1{
    Txonly( int ntvals, double *txval, double *tyval ):
      m_ntvals( ntvals ),
      m_txval( txval ),
      m_tyval( tyval )
    {}
    double operator() (double t) const 
    { return linfuncint(t, m_ntvals, m_txval, m_tyval ); }
    int m_ntvals;
    double *m_txval, *m_tyval;
  };
  /*
    double tPfunc(double t,double y)
    {
    return quadfuncint(t,ntvals,txval,tyval)-y;
    }
  */
  struct TPfunc: public F2{
    TPfunc( int ntvals, double *txval, double *tyval ):
      m_ntvals( ntvals ),
      m_txval( txval ),
      m_tyval( tyval )
    {}
    double operator() (double t, double y) const 
    { return quadfuncint(t, m_ntvals, m_txval, m_tyval)-y; }
    int m_ntvals;
    double *m_txval, *m_tyval;
  };
}}

#endif
