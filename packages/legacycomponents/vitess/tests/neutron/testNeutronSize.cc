#include <iostream>

typedef double VectorType[3];

typedef struct
{
  char          IDGrp[2];
  unsigned long IDNo;
}
TotalID;

typedef struct
{
  TotalID       ID;
  char          Debug;
  short         Color;
  double        Time;
  double        Wavelength;
  double        Probability;
  VectorType    Position;
  VectorType    Vector;
  VectorType    Spin;
}
Neutron;

int main()
{
  /*
  std::cout << sizeof(Neutron::ID) << std::endl;
  std::cout << sizeof(TotalID::IDGrp) << std::endl;
  std::cout << sizeof(TotalID::IDNo) << std::endl;
  std::cout << sizeof(Neutron::Debug) << std::endl;
  std::cout << sizeof(Neutron::Color) << std::endl;
  */
  std::cout << sizeof(Neutron) << std::endl;
}
