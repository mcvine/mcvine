/***************ideal powder sample********************
* construct idea powderN sample from McStas PowderN
* only consider scattering process
* no absorption and sample geometry are taken into account
*/


class line_data
{
 public:
  const line_data& operator=(const line_data&);
  static std::vector<line_data> FromString(const char** data, double DW_v, double w_v);

 public:
  double F2;                  /* Value of squared structure factor */
  double q;                   /* Qvector */
  int j;                      /* Multiplicity */
  double DWfactor;            /* Debye-Waller factor */
  double w;                   /* Intrinsic line width */ 
};


class line_info_struct
{
 public:
  bool get_intensity(double* q_v, double* w_v, double* my_s_v2) const;
  
 public:
  std::vector<line_data> list; /* Reflection array */
  double Dd;             /*relative line width Delta_d/d, when 'w' is not available*/
  double DWfactor;       /*Debye-Waller factor*/
  double V_0;            /*Volume of unit cell [Angstrom^3]*/  
  double rho;            /*density of material. [g/cm^3]*/
  double at_weight;      /*atomic/molecular weight of material [g/mol]*/
  double at_nb;          /*number of atoms per unit cell*/
  double sigma_a;        /*Absorption cross section per unit cell at 2200m/s [barns]*/
  double sigma_i;        /*Incoherent cross section per unit cell [barns]*/
};


class scatter_kernel
{
 public:
  scatter_kernel(const line_info_struct& line_info);  //constructor
  ~scatter_kernel();                                  //deconstructor
  void set_velocity(double vx1, double vy1, double vz1) {vx = vx1; vy = vy1; vz = vz1;}
  void scatter(double& out_vx, double& out_vy, double& out_vz, double& scatter_i, double d_phi=0);

 private:
  double vx;
  double vy;
  double vz;
  double* q_v;
  double* w_v;
  double* my_s_v2;
  int Nq;
};

