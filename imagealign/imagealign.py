# -*- coding: utf-8 -*-

from scipy import misc
import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la

#Load good photo
faceOriginal = misc.face()
faceOriginal = misc.imread('D:\\Online Courses\\NumericalAnalysis\\imagealign\\deskOriginal.png')

figOrig = plt.figure()
ax = figOrig.add_subplot(111)
ax.imshow(faceOriginal)

coordsOriginal = []
coordsSkewed = []

def onclickOriginal(event):
    coordsOriginal.append((event.x, event.y))
    
cidOrig = figOrig.canvas.mpl_connect('button_press_event', onclickOriginal)

#Load bad photo
faceSkewed = misc.face()
faceSkewed = misc.imread('D:\\Online Courses\\NumericalAnalysis\\imagealign\\deskSkewed.png')
figSkewed = plt.figure()
ax = figSkewed.add_subplot(111)
ax.imshow(faceSkewed)

coordsOriginal = []
coordsSkewed = []

def onclickSkewed(event):
    coordsSkewed.append((event.x, event.y))
    
cidSkewed = figSkewed.canvas.mpl_connect('button_press_event', onclickSkewed)

def compute_rigid_transform(refpoints, points):
    A = np.array([
                [points[0][0], -points[0][1], 1, 0],
                [points[0][1], points[0][0], 0, 1],
                [points[1][0], -points[1][1], 1, 0],
                [points[1][1], points[1][0], 0, 1],
                [points[2][0], -points[2][1], 1, 0],
                [points[2][1], points[2][0], 0, 1],
                [points[3][0], -points[3][1], 1, 0],
                [points[3][1], points[3][0], 0, 1],
                [points[4][0], -points[4][1], 1, 0],
                [points[4][1], points[4][0], 0, 1],
                [points[5][0], -points[5][1], 1, 0],
                [points[5][1], points[5][0], 0, 1]
            ])
    y = np.array([
                refpoints[0][0],
                refpoints[0][1],
                refpoints[1][0],
                refpoints[1][1],
                refpoints[2][0],
                refpoints[2][1],
                refpoints[3][0],
                refpoints[3][1],
                refpoints[4][0],
                refpoints[4][1],
                refpoints[5][0],
                refpoints[5][1]
            ])
    a, b, tx, ty = la.lstsq(A, y)[0]
    R = np.array([[a, b], [-b, a]])
    return R, tx, ty

#Part 2
from scipy import ndimage
from scipy.misc import imsave

def rigid_alignment(coordsOriginal, coordsSkewed):
    R, tx, ty = compute_rigid_transform(coordsOriginal, coordsSkewed)
    T = np.array([[R[1][1], R[1][0]], [R[0][1], R[0][0]]])
    im = np.array(faceSkewed)
    im2 = np.zeros(im.shape, 'uint8')
    
    for i in range(len(im.shape)):
        im2[:, :, i] = ndimage.affine_transform(im[:, :, i], la.inv(T))
    plt.imshow(im2)
        
rigid_alignment(coordsOriginal, coordsSkewed)
    
    
    
    
    
    
    
    