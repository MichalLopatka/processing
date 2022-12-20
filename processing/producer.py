from processing.source import Source
from time import sleep
from queue import Queue
import logging

log = logging.getLogger(__name__)


class Producer:
    """
    Producer class, creating 3 channel random images using Source class
    params rows, cols, channels: gieb dimentions
    """

    def __init__(self, rows: int = 1024, cols: int = 768, channels: int = 3):
        self.source_shape = (rows, cols, channels)
        self.source = Source(self.source_shape)

    def get_frame(self):
        """
        Gets data from source
        return: frame from source
        """
        return self.source.get_data()

    def download_frames(self, queue: Queue, count: int = 100, rate: float = 0.05):
        """
        Generates images using Source and puts to a queue at given rate
        param queue: Queue to put images
        param count: Number of frames to generate
        rate: time interval between generating frames
        """
        for i in range(count):
            frame = self.get_frame()
            log.info(f"produced {i}")
            sleep(rate)
            queue.put(frame)
