//--C++--
//-- elliptical cylinder 1D analytical = no orientation
//-- SANS

#include <boost/python.hpp> 

#include "mccomponents/kernels/sample/AbstractSQ.h" 
#include "mccomponents/kernels/sample/SQAdaptor.h" 
 
extern "C" { 
#include "sans/elliptical_cylinder.h" 
} 

namespace wrap_models{
struct Elliptical_cylinder{
	Elliptical_cylinder(double scale,double r_minor, double r_ratio, double length, double contrast, double background,double cyl_theta, double cyl_phi,double cyl_psi) 
	{
    p.scale = scale;
    p.r_minor = r_minor;
	p.r_ratio = r_ratio;
	p.length = length;
    p.contrast = contrast;
	p.background = background;
    p.cyl_theta = cyl_theta;
	p.cyl_phi = cyl_phi;
	p.cyl_psi = cyl_psi;
	} 

	double operator() (double q) const
	{
		return elliptical_cylinder_analytical_1D( const_cast<EllipticalCylinderParameters *>(&p), q);
	}
	EllipticalCylinderParameters p;
};

  
void wrap_elliptical_cylinder() 
{ 
	using namespace boost::python; 
	typedef Elliptical_cylinder w_t; 
	class_<w_t> 
		(  
		"SANSModel_Elliptical_cylinder", 
		init< double, double, double, double, double, double, double, double, double >() 
			) 
		; 

	using namespace mccomponents::sample; 
	typedef SQAdaptor<w_t> SQ; 
	class_<SQ, bases<AbstractSQ> > 
		( 
		"SANSModel_Elliptical_cylinder_SQAdaptor", 
		init< const w_t & >() 
		[with_custodian_and_ward<1,2>()] //Jiao, what you mean by the numbers,<1,2>???
		) 
		; 
	} 
} 
//2009-06-02 jhcho
// End of file
