/***************ideal powder sample********************
* construct idea powderN sample from McStas PowderN
* only consider scattering process
* no absorption and sample geometry are taken into account
*/

#include <iostream>
#include <cmath>
#include <vector>
#include "Rand_generator/mcstas_lib.h"
#include "Ideal_PowderN.v1.h"
using namespace std;

#define PI 3.14159

double DEG2RAD = PI/180.0;
double V2K = (1.67e-27)/(6.63e-34/2/PI);//*pow(10.0,10.0);
double K2V = 1/V2K;
double pack = 1.0;
double XsectionFactor = 1.0;


const line_data& line_data::operator=(const line_data& rhs)
{
  if(&rhs == this)
    return *this;
  F2 = rhs.F2;
  q = rhs.q;
  j = rhs.j;
  DWfactor = rhs.DWfactor;
  w = rhs.w;
  return *this;
}


//std::pair<line_data*,int> line_data::FromString(const char** data, double DW_v, double w_v)
std::vector<line_data> line_data::FromString(const char** data, double DW_v, double w_v)
{
  std::vector<line_data> datalist; /*vector of pointers to class*/
  for(int i=1; true; i++)
    {
      if(strlen(data[i]) == 0)
	break;

      double F2, d_spacing;
      int j;      
      sscanf(data[i], "%lf %lf %d", &d_spacing, &F2, &j);  //to be corrected
      
      //line_data* ld = new line_data(); 
      line_data ld;
      ld.q = 1 / d_spacing * pow(10.0,10.0);
      ld.F2 = F2 * F2;        
      ld.j = j;
      ld.DWfactor = DW_v;      //use constant
      ld.w = w_v;            //use constant
      datalist.push_back(ld);
      //delete ld;               //release freestore
    }
  /*
  line_data* result = new line_data[datalist.size()]; //pointer to an array of class
  //line_data* p_result = result;                       //p_result points to result[0]
  
  for(int i=0; i<datalist.size(); i++)
    {
      result[i] = *(datalist[i]);
      //p_result = datalist[i];
      //p_result++;
    }
  return std::pair<line_data*,int>(result, datalist.size());
  */
  return datalist;
}


bool line_info_struct::get_intensity(double* q_v, double* w_v, double* my_s_v2) const
{
  const std::vector<line_data> L = list;

  int Nq  = list.size();
  if (!q_v || !w_v || !my_s_v2)
    //exit(fprintf(stderr,"PowderN: %s: ERROR allocating memory (init)\n", NAME_CURRENT_COMP));
    return false;

  for(int i=0; i<Nq; i++)
    {
      my_s_v2[i] = 4*PI*PI*PI*pack*(L[i].DWfactor ? L[i].DWfactor : 1)
	/(V_0*V_0*V2K*V2K)
	*(L[i].j * L[i].F2 / L[i].q)*XsectionFactor;
      /* Is not yet divided by v^2 */
      /* Squires [3.103] */
      q_v[i] = L[i].q*K2V;
      w_v[i] = L[i].w;
    }
  
  /* Is not yet divided by v */
  double my_a_v = pack*sigma_a/V_0*2200*100;   // Factor 100 to convert from barns to fm^2
  double my_inc = pack*sigma_i/V_0*100;   // Factor 100 to convert from barns to fm^2
}


scatter_kernel::scatter_kernel(const line_info_struct& line_info)
{
    Nq = line_info.list.size();
    q_v = new double[Nq];
    w_v = new double[Nq];
    my_s_v2 = new double[Nq];
    line_info.get_intensity(q_v, w_v, my_s_v2); 
}


scatter_kernel::~scatter_kernel()
{
  delete [] q_v;
  delete [] w_v;
  delete [] my_s_v2;
}

void scatter_kernel::scatter(double& out_vx, double& out_vy, double& out_vz, double& scatter_i, double d_phi)
/*d_phi is not used quite often. It is used to relate 
  the height of detector to the Debye-Sherrer cone*/
{
  int line;
  double arg;
  double alpha;
  double theta;
  double alpha0;
  int nx, ny, nz;
  
  double v = sqrt(vx*vx + vy*vy + vz*vz);
  /* Make coherent scattering event */

  if (Nq > 0) {
    /* choose line */
    if (Nq > 1) 
      {
	line=floor(Nq*rand01());  /* Select between Nq powder lines */
      }
    else line = 0;
    if (w_v[line])
      {
	arg = q_v[line]*(1+w_v[line]*randpm1())/(2.0*v); /*normal*/
	cout << "arg: " << arg << endl;
      }
    else
      arg = q_v[line]/(2.0*v);
    scatter_i= my_s_v2[line]/(v*v);
    //cout << "intensity: " << scatter_i << endl;
    /*absorption is ignored.*			
      }
      if (d_phi != 0) {
      /* Focusing */
    theta = asin(arg);

    /* Choose point on Debye-Scherrer cone */
    if (d_phi)
      { /* relate height of detector to the height on DS cone */
	arg = sin(d_phi*DEG2RAD/2)/sin(2*theta);
	/* If full Debye-Scherrer cone is within d_phi, don't focus */
	if (arg < -1 || arg > 1) d_phi = 0;
	/* Otherwise, determine alpha to rotate from scattering plane
	   into d_phi focusing area*/
	else alpha = 2*asin(arg);
      }
    if (d_phi) {
      /* Focusing */
      alpha = fabs(alpha);
      /* Trick to get scattering for pos/neg theta's */
      alpha0= 2*rand01()*alpha;
      if (alpha0 > alpha) {
	alpha0=PI+(alpha0-1.5*alpha);
      } else {
	alpha0=alpha0-0.5*alpha;
      }
    }
    else
      alpha0 = PI*randpm1();

    alpha = fabs(alpha);

    /* Trick to get scattering for pos/neg theta's */
    alpha0= 2*rand01()*alpha;
    if (alpha0 > alpha) {
      alpha0=PI+(alpha0-1.5*alpha);
    } else {
      alpha0=alpha0-0.5*alpha;
    }
  }
  else
    {
      alpha0 = PI*randpm1();
      cout << "angle: " << alpha0 << endl;
    }
  /* now find a nearly vertical rotation axis:
   * Either
   *  (v along Z) x (X axis) -> nearly Y axis
   * Or
   *  (v along X) x (Z axis) -> nearly Y axis
   */
  if (fabs(scalar_prod(1,0,0,vx/v,vy/v,vz/v)) < fabs(scalar_prod(0,0,1,vx/v,vy/v,vz/v))) 
    {
      nx = 1; ny = 0; nz = 0;
    } 
  else 
    {
      nx = 0; ny = 0; nz = 1;
    }
  double tmp_vx, tmp_vy, tmp_vz;
  vec_prod(tmp_vx,tmp_vy,tmp_vz, vx,vy,vz, nx,ny,nz);
  
  /* v_out = rotate 'v' by 2*theta around tmp_v: Bragg angle */
  double vout_x, vout_y, vout_z;
  rotate(vout_x,vout_y,vout_z, vx,vy,vz, 2*theta, tmp_vx,tmp_vy,tmp_vz);
  
  /* tmp_v = rotate v_out by alpha0 around 'v' (Debye-Scherrer cone) */
  rotate(tmp_vx,tmp_vy,tmp_vz, vout_x,vout_y,vout_z, alpha0, vx, vy, vz);
  out_vx = tmp_vx;
  out_vy = tmp_vy;
  out_vz = tmp_vz;
}
