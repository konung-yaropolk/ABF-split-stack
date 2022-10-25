#!/usr/bin/env python3

from itertools import zip_longest
import numpy as np 
import pyabf
import settings as s


s.MIN_X*=s.FREQ
s.MAX_X*=s.FREQ
s.STEP*=s.FREQ

def convert(filename, sweep_n):

    abf = pyabf.ABF(filename)
    abf.setSweep(sweep_n, 0)
    buffer_array = abf.sweepY.copy()
    template = pyabf.ABF(s.TEMPLATE_ABF)    
    
    for i in range(s.COUNT):
        template.setSweep(i, 0)
        template.sweepY[0: s.MAX_X-s.MIN_X] = buffer_array[s.MIN_X + s.STEP*i : s.MAX_X + s.STEP*i]

    
    template.saveABF1(filename + '_training_series_splitted_by_sweeps.abf', s.OUTPUT_FREQ*1000)
    print(filename, ' proceed successfull')

for path, sweep_number in s.QUEUE:
    try:
        convert(s.DIR+path, sweep_number)
    except:
        print(path, ' ERROR, wrong path or floating point ABF file!!!')

print('\nQueue proceed successfull')
