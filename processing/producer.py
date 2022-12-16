from processing.source import Source


class Producer:
    def __init__(self, rows: int = 1024, cols: int = 768, channels: int = 3):
        self.source_shape = (rows, cols, channels)
        self.source = Source(self.source_shape)

    def download_frame(self):
        frame = self.source.get_data()
        return frame
