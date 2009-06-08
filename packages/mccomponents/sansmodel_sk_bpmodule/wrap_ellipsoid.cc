//--C++--
//-- ellipsoid 1D analytical = no orientation
//-- SANS

#include <boost/python.hpp> 

#include "mccomponents/kernels/sample/AbstractSQ.h" 
#include "mccomponents/kernels/sample/SQAdaptor.h" 
 
extern "C" { 
#include "sans/ellipsoid.h" 
} 

namespace wrap_models{
struct Ellipsoid{
	Ellipsoid(double scale,double radius_a, double radius_b, double contrast, double background,double axis_theta, double axis_phi) 
	{
    p.scale = scale;
    p.radius_a = radius_a;
	p.radius_b = radius_b;
    p.contrast = contrast;
	p.background = background;
    p.axis_theta = axis_theta;
	p.axis_phi = axis_phi;
	} 

	double operator() (double q) const
	{
		return ellipsoid_analytical_1D( const_cast<EllipsoidParameters *>(&p), q);
	}
	EllipsoidParameters p;
};

  
void wrap_ellipsoid() 
{ 
	using namespace boost::python; 
	typedef Ellipsoid w_t; 
	class_<w_t> 
		(  
		"SANSModel_Ellipsoid", 
		init< double, double, double, double, double, double, double >() 
			) 
		; 

	using namespace mccomponents::sample; 
	typedef SQAdaptor<w_t> SQ; 
	class_<SQ, bases<AbstractSQ> > 
		( 
		"SANSModel_Ellipsoid_SQAdaptor", 
		init< const w_t & >() 
		[with_custodian_and_ward<1,2>()] //Jiao, what you mean by the numbers,<1,2>???
		) 
		; 
	} 
} 
//2009-06-02 jhcho
// End of file