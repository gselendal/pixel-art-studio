from PIL import Image, ImageFilter
from scipy import misc, ndimage
import matplotlib.pyplot as plt
import imageio
import math
import numpy as np

face = misc.face()
imageio.imsave('face.png', face)
face = imageio.imread('face.png')


def create_pixel_art(img):
    _w = (img.shape[1])
    w = _w
    w = w - w % 10

    _h = img.shape[0]
    h = _h
    h = h - h % 10
    step_size = min(25, math.gcd(w, h))

    cols = []

    for i in range(_w):
        if (not(i % step_size < (step_size / 5))):
            cols.append(i)

    img = np.delete(img, cols, axis=1)

    rows = []

    for j in range(_h):
        if (not(j % step_size < (step_size / 5))):
            rows.append(j)

    img = np.delete(img, rows, axis=0)

    return img


pixel_face = create_pixel_art(face)
imageio.imsave('pixel_face.png', pixel_face)
