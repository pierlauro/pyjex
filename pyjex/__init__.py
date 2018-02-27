from __future__ import print_function
import sys
from traceback import extract_tb

sys.excepthook = lambda e, m, tb: print ( '{}: {}\n{}'.format( e.__name__, m, '\n'.join( [ '\tat {}({}:{})'.format(  t[2], t[0], t[1] ) for t in extract_tb( tb )[::-1] ] ) ), file = sys.stderr )
