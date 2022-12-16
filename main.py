from processing.producer import Producer

def main():
    producer = Producer()
    frame = producer.download_frame()
    print(frame)

if __name__ == "__main__":
    main()
