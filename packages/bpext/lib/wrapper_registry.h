#include <map>
#include "Python.h"

namespace bpext {
  typedef PyObject *(* Wrapper) ( void * );
  struct ltstr1
  {
    bool operator()(const char* s1, const char* s2) const
    {
      return strcmp(s1, s2) < 0;
    }
  };  
  typedef std::map<const char *, Wrapper, ltstr1> WrapperRegistry;
  extern WrapperRegistry wrapperRegistry;
}
