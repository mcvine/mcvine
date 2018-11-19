#include "mccomponents/kernels/sample/SQ/SQ_fromexpression.h"


mccomponents::sample::SQ_fromexpression::SQ_fromexpression
( const std::string & expr )
{
  std::string vars = "Q";
  int res = m_fparser.Parse(expr, vars);
  if (res >=0 ) {
    throw BadExpression(expr);
  }
}

