from processing.producer import Producer
from processing.consumer import Consumer


def main():
    producer = Producer()
    consumer = Consumer()
    frame = producer.download_frame()
    print(frame.shape)
    resized = consumer.resize(frame)
    print(resized.shape)
    filtered = consumer.apply_median(resized)
    print(filtered.shape)
    consumer.save(resized, "./processed/t1")
    consumer.save(filtered, "./processed/t2")

if __name__ == "__main__":
    main()
