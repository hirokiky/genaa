import itertools
import sys

import genaa

PY3 = sys.version_info[0] == 3

if PY3:
    zip_longest_ = itertools.zip_longest

    def u(s):
        return s
else:
    zip_longest_ = itertools.izip_longest

    def u(s):
        return unicode(s, encoding=genaa.ENCODING)
