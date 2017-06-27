# -*- coding: utf-8 -*-
"""
Created on Tue Jun 27 10:47:17 2017

@author: Alexandru Meterez
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def Circle(x, y, p):
    return (pow(pow(abs(x), p) + pow(abs(y), p), 1/p))

xx = np.linspace(-2, 2, 400)
yy = np.linspace(-2, 2, 400)
[X, Y] = np.meshgrid(xx, yy)
Z = Circle(X, Y, 1)

fig = plt.figure()
ax = fig.add_subplot(111)
fig.subplots_adjust(left = 0.25, bottom = 0.25)
line = ax.contour(X, Y, Z, [1])

#Adding the sliders
normSliderAx = fig.add_axes([0.25, 0.15, 0.65, 0.03])
normSlider = Slider(normSliderAx, 'p-norm', 1, 30, valinit = 1)
def sliders_on_changed(val):
    ax.clear()
    line = []
    line = ax.contour(X, Y, Circle(X, Y, val), [1])
    
normSlider.on_changed(sliders_on_changed)
plt.show()