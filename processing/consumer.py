import numpy as np
from scipy import ndimage
import cv2 

class Consumer:
    def resize(self, inp: np.ndarray, coeff: int = 2):
        resized = inp[::coeff, ::coeff]
        return resized

    def apply_median(self, image: np.ndarray, size: int = 5):
        filtered = ndimage.median_filter(image, size=size)
        return filtered

    def save(self, image, name):
        cv2.imwrite(f"{name}.png", image)