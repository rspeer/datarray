
try:
    from numpy.testing import Tester
    test = Tester().test
    del Tester
except (ImportError, ValueError):
    print "No datarray unit testing available."
    
from version import __version__
from datarray import DataArray
