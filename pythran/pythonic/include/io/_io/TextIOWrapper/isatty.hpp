#ifndef PYTHONIC_INCLUDE_IO__IO_TEXTIOWRAPPER_ISATTY_HPP
#define PYTHONIC_INCLUDE_IO__IO_TEXTIOWRAPPER_ISATTY_HPP

#include "pythonic/include/__builtin__/file/isatty.hpp"

namespace pythonic
{

  namespace io
  {

    namespace _io
    {
      namespace TextIOWrapper
      {
        USING_FUNCTOR(isatty, __builtin__::file::functor::isatty);
      }
    }
  }
}
#endif
