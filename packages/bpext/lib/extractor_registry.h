#include <map>
#include "Python.h"

namespace bpext {
  typedef void *(* Extractor) ( PyObject * );
  struct ltstr
  {
    bool operator()(const char* s1, const char* s2) const
    {
      return strcmp(s1, s2) < 0;
    }
  };  
  typedef std::map<const char *, Extractor, ltstr> ExtractorRegistry;
  extern ExtractorRegistry extractorRegistry;
}
