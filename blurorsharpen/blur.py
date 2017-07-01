from scipy import ndimage
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np

face = misc.face()
face = misc.imread('face.png')

blurred_image = ndimage.uniform_filter(face, size = 10)

np.linalg.lstsq(blurred_image, face)