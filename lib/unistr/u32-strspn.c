/* Search for some characters in UTF-32 string.
   Copyright (C) 1999, 2002, 2006, 2009-2014 Free Software Foundation, Inc.
   Written by Bruno Haible <bruno@clisp.org>, 2002.

   This program is free software: you can redistribute it and/or modify it
   under the terms of the GNU Lesser General Public License as published
   by the Free Software Foundation; either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
   Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

#include <config.h>

/* Specification.  */
#include "unistr.h"

#define FUNC u32_strspn
#define UNIT uint32_t
#define U_STRCHR u32_strchr

size_t
FUNC (const UNIT *str, const UNIT *accept)
{
  /* Optimize two cases.  */
  if (accept[0] == 0)
    return 0;
  if (accept[1] == 0)
    {
      ucs4_t uc = accept[0];
      const UNIT *ptr = str;
      for (; *ptr != 0; ptr++)
        if (*ptr != uc)
          break;
      return ptr - str;
    }
  /* General case.  */
  {
    const UNIT *ptr = str;
    for (; *ptr != 0; ptr++)
      if (!U_STRCHR (accept, *ptr))
        break;
    return ptr - str;
  }
}
