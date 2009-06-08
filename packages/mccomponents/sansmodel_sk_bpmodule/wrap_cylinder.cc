//--C++--
//-- cylinder 1D analytical = no orientation
//-- SANS

#include <boost/python.hpp> 

#include "mccomponents/kernels/sample/AbstractSQ.h" 
#include "mccomponents/kernels/sample/SQAdaptor.h" 
 
extern "C" { 
#include "sans/cylinder.h" 
} 

namespace wrap_models{
struct Cylinder{
	Cylinder(double scale,double radius, double length, double contrast, double background,double cyl_theta, double cyl_phi) 
	{
    p.scale = scale;
    p.radius = radius;
	p.length = length;
    p.contrast = contrast;
	p.background = background;
    p.cyl_theta = cyl_theta;
	p.cyl_phi = cyl_phi;
	} 

	double operator() (double q) const
	{
		return cylinder_analytical_1D( const_cast<CylinderParameters *>(&p), q);
	}
	CylinderParameters p;
};

  
void wrap_cylinder() 
{ 
	using namespace boost::python; 
	typedef Cylinder w_t; 
	class_<w_t> 
		(  
		"SANSModel_Cylinder", 
		init< double, double, double, double, double, double, double >() 
			) 
		; 

	using namespace mccomponents::sample; 
	typedef SQAdaptor<w_t> SQ; 
	class_<SQ, bases<AbstractSQ> > 
		( 
		"SANSModel_Cylinder_SQAdaptor", 
		init< const w_t & >() 
		[with_custodian_and_ward<1,2>()] //Jiao, what you mean by the numbers,<1,2>???
		) 
		; 
	} 
} 
//2009-06-02 jhcho
// End of file