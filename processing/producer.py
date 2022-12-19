from processing.source import Source
from time import sleep


class Producer:
    def __init__(self, rows: int = 1024, cols: int = 768, channels: int = 3):
        self.source_shape = (rows, cols, channels)
        self.source = Source(self.source_shape)

    def download_frame(self, queue, count=20):
        for i in range(count):
            frame = self.source.get_data()
            print(f"produced {i}")
            sleep(0.05)
            queue.put(frame)
