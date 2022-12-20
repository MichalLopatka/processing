from processing.consumer import Consumer
import numpy as np
import os
import pytest
from queue import Queue
from threading import Thread


@pytest.fixture
def consumer():
    return Consumer()


@pytest.fixture
def arr():
    return np.random.randint(
        256,
        size=256 * 256 * 3,
        dtype=np.uint8,
    ).reshape(256, 256, 3)


def test_resizing(consumer, arr):
    resized = consumer.resize(arr, 4)
    assert resized.shape == (64, 64, 3)


def test_median(consumer, arr):
    filtered = consumer.apply_median(arr)
    assert np.array_equal(filtered, arr) is False


def test_saving(consumer, arr):
    filename = "test/data/test.png"
    try:
        os.remove(filename)
    except OSError:
        pass
    consumer.save_image(filename, arr)
    assert os.path.exists(filename) is True


def test_processing(consumer, arr):
    queue1 = Queue()
    queue2 = Queue()
    queue1.put(arr)
    queue1.put(arr)
    consumer_thread = Thread(
        target=consumer.process, args=(queue1, queue2), daemon=True
    )
    consumer_thread.start()
    queue1.join()
    assert queue1.qsize() == 0 and queue2.qsize() == 2


def test_saving_from_queue(consumer, arr):
    directory = "test/data/processed"
    pathfile = directory + "/0.png"
    try:
        os.remove(pathfile)
    except OSError:
        pass
    queue1 = Queue()
    queue1.put(arr)
    saving_thread = Thread(target=consumer.save, args=(queue1, directory), daemon=True)
    saving_thread.start()
    queue1.join()
    assert os.path.exists(pathfile) is True
