// -*- C++ -*-
// Jiao Lin <jiao.lin@gmail.com>

#ifndef MCCOMPONENTS_MATH_SEARCH_H
#define MCCOMPONENTS_MATH_SEARCH_H

#include <vector>

namespace mccomponents{
  namespace math{
    // assuming xs is increasing, find the first bin in xs that is larger than x
    template <typename num_t, typename iterator_t>
    num_t find_1st_bin_larger_than(num_t x, iterator_t xstart, iterator_t xend);
  }
}

#include "search.icc"
#endif
