//test file for sample kernel powderN
#include <iostream>
#include <cmath>
#include <vector>
#include "Rand_generator/mcstas_lib.h"
#include "Ideal_PowderN.v1.h"
#include <ctime>
using namespace std;


	//double F2;                  /* Value of structure factor */
	//double q;                   /* Qvector */
	//int j;                      /* Multiplicity */
	//double DWfactor(1);            /* Debye-Waller factor */
	//double w(1%);                   /* Intrinsic line width */




const char* test_line_data[100] = {
	"D-VALUE(q)   F(HKL)(F2)   MULT(j)",
	"3.1353      3.3     8",
	"1.9200      0.0    12",
	"1.6374      3.2    24",
	"1.5677      6.3     8",
	"1.3576      6.2     6",
	"1.2458      3.1    24",
	"1.1085      0.0    24",
	"1.0451      2.9    24",
	"1.0451      2.9     8",
	"0.9600      5.7    12",
	"0.9179      2.8    48",
	"0.9051      0.0    24",
	"0.8586      0.0    24",
	"0.8281      2.7    24",
	"0.8187      5.4    24",
	"0.7838      5.3     8",
	"0.7604      2.6    24",
	"0.7604      2.6    24",
	"0.7257      0.0    48",
	"0.7070      2.5    24",
	"0.7070      2.5    48",
	"0.6788      5.0     6",
	"0.6634      2.4    24",
	"0.6585      0.0    24",
	"0.6400      0.0    12",
	"0.6400      0.0    24",
	"0.6271      2.4    48",
	"0.6271      2.4     8",
	"0.6229      4.7    24",
	"0.6072      4.6    24",
	"0.5961      2.3    48",
	"0.5961      2.3    24",
	"0.5925      0.0    48",
	"0.5789      0.0    24",
	"0.5693      2.2    48",
	"0.5543      4.3    24",
	"0.5458      2.1    24",
	"0.5458      2.1    24",
	"0.5458      2.1    24",
	"0.5325      0.0    24",
	"0.5325      0.0    48",
	"0.5250      2.0    48",
	"0.5250      2.0    24",
	"0.5226      4.1    24",
	"0.5226      4.1     8",
	""
};



int main()
{
  std::vector<line_data> ld = line_data::FromString(test_line_data, 1.0, 0.0);
  line_info_struct lis;
  lis.list = ld;
  //lis.count = ld.second;
  lis.Dd = 1e-5;
  lis.DWfactor = 1.0;
  lis.V_0 = 5.43053*5.43053*5.43053;//*10e-30;
  lis.rho = 2.33;
  lis.at_weight = 28.08;
  lis.at_nb = 16;
  lis.sigma_a = 0.171;
  lis.sigma_i = 0.004;
  //strcpy(lis.compname, "");
  //lis.flag_barns = 1.0;
  //strcpy(lis.column_order, "");

  srand(time(NULL));

  scatter_kernel SK(lis);

  for (int i=0; i<1000; i++)
    {
      double vx=5.0*randpm1(), vy=5.0*randpm1(), vz=rand_range(1000.0, 3000.0);
      //cout << "vx, vy, vz before scattering: " << vx <<" "<< vy << " "<< vz << endl; 
      double out_vx, out_vy, out_vz, scatter_i;
      double d_phi = 0;
      

      SK.set_velocity(vx, vy, vz);
      SK.scatter(out_vx, out_vy, out_vz, 
		 scatter_i, d_phi);
      
      //cout << out_vx<<" "<< out_vy<<" "<<out_vz << endl;
      if (vz != out_vz)
	{
	  cout << "find one! " << i <<endl;
	  cout << "vx, vy, vz before scattering: " << vx <<" "<< vy << " "<< vz 
	       << " total: "<< sqrt(vx*vx+vy*vy+vz*vz)<<endl;
	  cout << "after scattering: " << out_vx<<" "<< out_vy<<" "<<out_vz << " total: "
	       << sqrt(out_vx*out_vx+out_vy*out_vy+out_vz*out_vz)<< endl;
	  cout << "intensity: " << scatter_i << endl;
	}
    }
  
  char s[] = "12.1 13";
  float a1;
  int a2;
  sscanf(s, "%f %d", &a1, &a2);
  cout << a1 <<" " << a2 << endl;

}

