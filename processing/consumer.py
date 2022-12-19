import numpy as np
from scipy import ndimage
import cv2
from time import sleep
from queue import Empty


class Consumer:
    def resize(self, inp: np.ndarray, coeff: int = 2):
        resized = inp[::coeff, ::coeff]
        return resized

    def apply_median(self, image: np.ndarray, size: int = 5):
        filtered = ndimage.median_filter(image, size=size)
        return filtered

    def save(self, queueB):
        no = 0
        while True:
            try:
                image = queueB.get()
                cv2.imwrite(f"processed/{no}.png", image)
                no += 1
            except Empty:
                continue
            else:
                print(f"saving item {no}")
                # sleep(0.05)
                queueB.task_done()

    def process(self, queueA, queueB):
        while True:
            try:
                item = queueA.get()
                resized = self.resize(item)
                filtered = self.apply_median(resized)
                queueB.put(filtered)
            except Empty:
                continue
            else:
                print(f"Processing item {item[0]}")
                # sleep(0.05)
                queueA.task_done()
