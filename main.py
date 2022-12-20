from processing.producer import Producer
from processing.consumer import Consumer
from threading import Thread
from queue import Queue
import logging

logging.basicConfig(filename="logs/processed.log", level=logging.INFO)
log = logging.getLogger(__name__)

logging.info("Started")


def run():
    producer = Producer()
    consumer = Consumer()
    A = Queue()
    B = Queue()
    producer_thread = Thread(target=producer.download_frames, args=(A,))
    producer_thread.start()
    consumer_thread = Thread(target=consumer.process, args=(A, B), daemon=True)
    consumer_thread.start()
    saving_thread = Thread(target=consumer.save, args=(B,), daemon=True)
    saving_thread.start()
    producer_thread.join()
    A.join()
    B.join()


def main():
    run()


if __name__ == "__main__":
    main()
