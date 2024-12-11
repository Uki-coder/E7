import matplotlib as mpl
mpl.use('TkAgg')
from calc import *

calc('input/B1z/b.txt','input/B1z/z.txt',\
     'input/B1I/b.txt', 'input/B1I/i.txt',
     'output/b1i/koeffs.txt', 'output/b1i/mu.txt',\
     'output/b1i/errors.txt', 20.5, 300, 194,1)

calc('input/B2z/b.txt','input/B2z/z.txt',\
     'input/B2I/b.txt', 'input/B2I/i.txt',
     'output/b2i/koeffs.txt', 'output/b2i/mu.txt',\
     'output/b2i/errors.txt', 13, 75, 194,3)