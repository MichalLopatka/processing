import numpy as np
from scipy import ndimage
import cv2
from queue import Empty, Queue
import logging

log = logging.getLogger(__name__)


class Consumer:
    """
    Class for processing given images
    """

    def resize(self, inp: np.ndarray, coeff: int = 2) -> np.ndarray:
        """
        Resizes given image
        param image: input image to resize
        param coeff: integer resizing coefficient
        returns: resized image
        """
        resized = inp[::coeff, ::coeff]
        return resized

    def apply_median(self, image: np.ndarray, size: int = 5) -> np.ndarray:
        """
        Applies median filter to given image
        param image: input image to filter
        param size: size of a filter
        returns: image with filter applied
        """
        filtered = ndimage.median_filter(image, size=size)
        return filtered

    def process(self, queueA: Queue, queueB: Queue):
        """
        Applies resizing and filtering to images taken from a queue a puts to another one
        param queueA: source queue
        param queueB: destination queue
        """
        no = 0
        while True:
            try:
                item = queueA.get()
                resized = self.resize(item)
                filtered = self.apply_median(resized)
                queueB.put(filtered)
                no += 1
            except Empty:
                continue
            else:
                log.info(f"Processed {no}")
                queueA.task_done()

    def save(self, queueB: Queue, directory: str = "data/processed"):
        """
        Gets items from a queue and saves to a directory
        param queueB: source queue
        param directory: directory to save
        """
        no = 0
        while True:
            try:
                image = queueB.get()
                self.save_image(f"{directory}/{no}.png", image)
                no += 1
            except Empty:
                continue
            else:
                log.info(f"saving item {no}")
                queueB.task_done()

    def save_image(self, path: str, image: np.ndarray):
        """
        Saves an image to with given filename
        param path: directory with a filename
        param image: image to save
        """
        cv2.imwrite(path, image)
