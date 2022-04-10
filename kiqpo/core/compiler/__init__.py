__version__ = '0.7.7'

import sys
import logging

logger = logging.getLogger(__name__)

# Assert compatibility and redirect to legacy version on Python 2.7
ok = True
if sys.version_info[0] == 2:  # pragma: no cover
    if sys.version_info < (2, 7):
        raise RuntimeError('PScript needs at least Python 2.7')
    if type(b'') == type(''):  # noqa - will be str and unicode after conversion
        sys.modules[__name__] = __import__(__name__ + '_legacy')
        ok = False

# NOTE: The code for the parser is quite long, especially if you want
# to document it well. Therefore it is split in multiple modules, which
# are simply numbered 0, 1, 2, etc. Here in the __init__, we define
# which parser is *the* parser. This gives us the freedom to split the
# parser in smaller pieces if we want.
#
# In the docstring of every parser module we maintain a brief user-guide
# demonstrating the features defined in that module. In the docs these
# docstrings are combined into one complete guide.

# flake8: noqa

if ok:

    from .parser0 import Parser0, JSError
    from .parser1 import Parser1
    from .parser2 import Parser2
    from .parser3 import Parser3
    from .base import *

    from .functions import py2js, evaljs, evalpy, JSString
    from .functions import script2js, js_rename, create_js_module
    from .stdlib import get_full_std_lib, get_all_std_names
    from .stubs import RawJS, JSConstant, window, undefined


del logging, sys, ok
