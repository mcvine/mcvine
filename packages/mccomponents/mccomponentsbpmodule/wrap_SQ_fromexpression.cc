// -*- C++ -*-
//
//


#include <sstream>
#include <boost/python.hpp>
#include "mccomponents/kernels/sample/AbstractSQ.h"
#include "mccomponents/kernels/sample/SQ/SQ_fromexpression.h"


namespace wrap_mccomponents {

  using namespace mccomponents::sample;

  void wrap_SQ_fromexpression()
  {
    using namespace boost::python;

    typedef SQ_fromexpression w_t;

    class_<w_t, bases<mccomponents::sample::AbstractSQ>, boost::noncopyable >
      ("SQ_fromexpression",
       init<const char *>()
       )
      ;    
  }

}


// End of file 
