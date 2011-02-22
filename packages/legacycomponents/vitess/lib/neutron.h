#ifndef MCVINE_VITESS_NEUTRON_H
#define MCVINE_VITESS_NEUTRON_H


namespace vitess {

  typedef double VectorType[3];
  
  typedef struct
  {
    char           IDGrp[2];
    unsigned long  IDNo;
  } TotalID;
  
  typedef struct 
  {
    TotalID        ID;
    char           Debug;
    short          Color;
    double         Time;
    double         Wavelength;
    double         Probability;
    VectorType     Position;
    VectorType     Vector;
    VectorType     Spin;
  } Neutron;

} // vitess

#endif
