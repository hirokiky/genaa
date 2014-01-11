import itertools
import sys


PY3 = sys.version_info[0] == 3


if PY3:
    zip_longest_ = itertools.zip_longest
else:
    zip_longest_ = itertools.izip_longest
