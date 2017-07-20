// -*- C++ -*-
#ifndef MCCOMPONENTS_MATH_MISC_H
#define MCCOMPONENTS_MATH_MISC_H

#include <algorithm>
#include <numeric>
#include <iostream>
#include <vector>
#include <functional>


namespace misc{

  //! if b>0 return abs(a), else return -abs(a)
  const double sign( const double &a, const double &b ) ;

}//misc



namespace std{
  //copy from sgi
  template<class T> struct print : public unary_function<T, void>
  {
    print(ostream& out) : os(out), count(0) {}
    void operator() (T x) { 
      os << x << ' ';
      ++count;
    }
    ostream& os;
    int count;
  };

  // this is used to circumvent a bug in gcc
  template<class T> struct print_ : public unary_function<T, void>
  {
    print_(ostream& out) : os(out), count(0) {}
    void operator() (T x) { 
      x.print(os);
      os << ' '; 
      ++count;
    }
    ostream& os;
    int count;
  };
}



namespace mccomponents{ namespace math{

  template <typename NumType>
  NumType sum( const std::vector<NumType> & arr)
  {
    return std::accumulate( arr.begin(), arr.end(), 0.0);
  }

  template <typename Type>
  Type product( const std::vector<Type> & A )
  {
    return std::accumulate(A.begin(), A.end(), Type(1), std::multiplies<Type>());
  }

  template <class NumType>
  void divide( std::vector<NumType> & arr, NumType divider )
  {
    std::transform( arr.begin(), arr.end(), arr.begin(), 
		    std::bind2nd( std::divides<NumType>(), divider));
  }

  template <class NumType>
  void multiply( std::vector<NumType> & arr, NumType multiplier )
  {
    std::transform( arr.begin(), arr.end(), arr.begin(), 
		    std::bind2nd( std::multiplies<NumType>(), multiplier));
  }

  template <typename NumType>
  void normalize( std::vector<NumType> & arr)
  {
    NumType sum1 = sum<NumType>(arr);
    divide<NumType>( arr, sum1);
  }
}}



template <class T>
std::ostream & operator << ( std::ostream &os, const std::vector<T> & v)
{
  os << "[";
  for (size_t i=0; i<v.size(); i++)
    os << v[i] << ", ";
  os << "]";
  return os;
}

template <class T1, class T2>
std::ostream & operator << ( std::ostream &os, const std::pair<T1,T2> & p)
{
  os << "(" << p.first << "," << p.second << ")";
  return os;
}


#endif // MCCOMPONENTS_MATH_MISC_H
