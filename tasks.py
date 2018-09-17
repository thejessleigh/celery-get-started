import queue
import random
import time
import threading


_queue = queue.Queue(10)


class ProducerThread(threading.Thread):
    def run(self):
        numbers = range(5)
        global _queue

        while True:
            number = random.choice(numbers)
            _queue.put(number)
            print("Produced {}".format(number))
            time.sleep(random.random())


class ConsumerThread(threading.Thread):
    def run(self):
        global _queue
        while True:
            number = _queue.get()
            _queue.task_done()
            print("consumed {}".format(number))
            time.sleep(random.random())


producer = ProducerThread()
producer.daemon = True
producer.start()

consumer = ConsumerThread()
consumer.daemon = True
consumer.start()

while True:
    time.sleep(1)
