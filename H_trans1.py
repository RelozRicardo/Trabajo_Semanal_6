#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 21:31:02 2024

@author: ricardo
"""

# Librerías externas NumPy, SciPy y Matplotlib
from scipy.signal import TransferFunction
import matplotlib.pyplot as plt
import numpy as np


# Librería de TC2, esta la vas a usar mucho
from pytc2.sistemas_lineales import pzmap, GroupDelay, bodePlot

w0 = 22000
qq = 5
K = 1


my_tf = TransferFunction( [K*pow(w0/qq,3) , 0 , 0 , 0] , [1, 1.25*w0/qq , 3*pow(w0,2) + 1.534*pow(w0/qq,2) , 2.5*pow(w0,3)/qq + 0.715*pow(w0/qq , 3) , 3*pow(w0,4)+ 1.534*pow(w0,4)/pow(qq,2) , 1.25*pow(w0,5)/qq , pow(w0,6)])
#my_tf=TransferFunction([0.0057] , [])

plt.close('all')

bodePlot(my_tf, fig_id=1, filter_description = 'Q={:3.3f}'.format(qq) )

pzmap(my_tf, fig_id=2, filter_description = 'Q={:3.3f}'.format(qq)) #S plane pole/zero plot

GroupDelay(my_tf, fig_id=3, filter_description = 'Q={:3.3f}'.format(qq))