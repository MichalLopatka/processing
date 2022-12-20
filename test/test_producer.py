from processing.producer import Producer
from queue import Queue
import pytest
import numpy as np


@pytest.fixture
def producer():
    return Producer(1024, 768, 3)


@pytest.fixture
def arr():
    return np.random.randint(
        256,
        size=256 * 256 * 3,
        dtype=np.uint8,
    ).reshape(256, 256, 3)


def test_get_data(producer):
    frame = producer.get_frame()
    assert frame.shape == (1024, 768, 3)


def test_downloading_to_queue(arr, producer):
    queue1 = Queue()
    queue1.put(arr)
    queue1.put(arr)
    queue2 = Queue()
    producer.download_frames(queue2, 2)
    assert queue1.qsize() == queue2.qsize()
