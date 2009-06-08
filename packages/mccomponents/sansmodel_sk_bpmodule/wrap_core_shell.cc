//--C++--
//-- core_shell_sphere 1D analytical
//-- SANS

#include <boost/python.hpp> 

#include "mccomponents/kernels/sample/AbstractSQ.h" 
#include "mccomponents/kernels/sample/SQAdaptor.h" 
 
extern "C" { 
#include "sans/core_shell.h" 
} 

namespace wrap_models{
struct Core_shell{
	Core_shell(double scale,double radius, double thickness, double core_sld, double shell_sld,double solvent_sld, double background) 
	{
    p.scale = scale;
    p.radius = radius;
    p.thickness = thickness;
    p.core_sld = core_sld;
	p.shell_sld = shell_sld;
	p.solvent_sld = solvent_sld;
	p.background = background;
	} 

	double operator() (double q) const
	{
		return core_shell_analytical_1D( const_cast<CoreShellParameters *>(&p), q);
	}
	CoreShellParameters p;
};

  
void wrap_core_shell() 
{ 
	using namespace boost::python; 
	typedef Core_shell w_t; 
	class_<w_t> 
		(  
		"SANSModel_Core_shell", 
		init< double, double, double, double, double, double, double >() 
			) 
		; 

	using namespace mccomponents::sample; 
	typedef SQAdaptor<w_t> SQ; 
	class_<SQ, bases<AbstractSQ> > 
		( 
		"SANSModel_Core_shell_SQAdaptor", 
		init< const w_t & >() 
		[with_custodian_and_ward<1,2>()] 
		) 
		; 
	} 
} 
//2009-06-02 jhcho
// End of file
