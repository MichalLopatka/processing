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

    def download_frame(self, queue: Queue, count: int = 100, rate: float = 0.05):
        """
        Generates images using Source and puts to a queue at given rate
        param queue: Queue to put images
        param count: Number of frames to generate
        rate: time interval between generating frames
        """
        for i in range(count):
            frame = self.source.get_data()
            log.info(f"produced {i}")
            sleep(rate)
            queue.put(frame)
