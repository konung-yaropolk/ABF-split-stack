#!/usr/bin/env python3

from itertools import zip_longest
import numpy as np 
import pyabf
import settings as s


# converting ms to sample count
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
        template.sweepY[s.MIN_X : s.MAX_X] = buffer_array[s.MIN_X + s.STEP*i : s.MAX_X + s.STEP*i]

    
    template.saveABF1(filename + s.SAVE_FILE_NAME_ENDING)  # , s.OUTPUT_FREQ*1000) - to save in different samplerate
    print(filename, ' proceed successfull')

for path, sweep_number in s.FILES_LIST:
    try:
        convert(s.DIR+path, sweep_number)
    except Exception as e: print(e)

print('\nQueue proceed successfull')
