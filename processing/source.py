import numpy as np


class Source:
    """
    Given data source, can create a random numpy array in 3 dimentions
    """

    def __init__(self, source_shape: tuple):
        self._source_shape: tuple = source_shape

    def get_data(self) -> np.ndarray:
        """
        Generates random 3D array with given dimentions
        returns: random numpy array
        """
        rows, cols, channels = self._source_shape
        return np.random.randint(
            256,
            size=rows * cols * channels,
            dtype=np.uint8,
        ).reshape(self._source_shape)
