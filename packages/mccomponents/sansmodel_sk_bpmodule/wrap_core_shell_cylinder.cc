//--C++--
//-- core_shell_cylinder 1D analytical = no orientation
//-- SANS

#include <boost/python.hpp> 

#include "mccomponents/kernels/sample/AbstractSQ.h" 
#include "mccomponents/kernels/sample/SQAdaptor.h" 
 
extern "C" { 
#include "sans/core_shell_cylinder.h" 
} 

namespace wrap_models{
struct Core_shell_cylinder{
	Core_shell_cylinder(double scale,double radius, double thickness, double length, double core_sld, double shell_sld, double solvent_sld, double background,double axis_theta, double axis_phi) 
	{
    p.scale = scale;
    p.radius = radius;
	p.thickness = thickness;
	p.length = length;
	p.core_sld = core_sld;
	p.shell_sld = shell_sld;
	p.solvent_sld = solvent_sld;	
	p.background = background;
    p.axis_theta = axis_theta;
	p.axis_phi = axis_phi;
	} 

	double operator() (double q) const
	{
		return core_shell_cylinder_analytical_1D( const_cast<CoreShellCylinderParameters *>(&p), q);
	}
	CoreShellCylinderParameters p;
};

  
void wrap_core_shell_cylinder() 
{ 
	using namespace boost::python; 
	typedef Core_shell_cylinder w_t; 
	class_<w_t> 
		(  
		"SANSModel_Core_shell_cylinder", 
		init< double, double, double, double, double, double, double, double, double, double >() 
			) 
		; 

	using namespace mccomponents::sample; 
	typedef SQAdaptor<w_t> SQ; 
	class_<SQ, bases<AbstractSQ> > 
		( 
		"SANSModel_Core_shell_cylinder_SQAdaptor", 
		init< const w_t & >() 
		[with_custodian_and_ward<1,2>()] //Jiao, what you mean by the numbers,<1,2>???
		) 
		; 
	} 
} 
//2009-06-02 jhcho
// End of file
