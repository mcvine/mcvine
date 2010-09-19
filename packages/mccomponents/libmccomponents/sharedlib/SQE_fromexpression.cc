#include "mccomponents/kernels/sample/SQE/SQE_fromexpression.h"


mccomponents::sample::SQE_fromexpression::SQE_fromexpression
( const std::string & expr )
{
  std::string vars = "Q,E";
  int res = m_fparser.Parse(expr, vars);
  if (res >=0 ) {
    throw BadExpression(expr);
  }
}

