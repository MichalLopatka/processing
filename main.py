from processing.producer import Producer
from processing.consumer import Consumer
from threading import Thread
from queue import Queue


def main():
    producer = Producer()
    consumer = Consumer()
    A = Queue()
    B = Queue()
    producer_thread = Thread(target=producer.download_frame, args=(A,))
    producer_thread.start()
    consumer_thread = Thread(target=consumer.process, args=(A, B), daemon=True)
    consumer_thread.start()
    producer_thread.join()

    saving_thread = Thread(target=consumer.save, args=(B,), daemon=True)
    saving_thread.start()
    A.join()
    B.join()


if __name__ == "__main__":
    main()
