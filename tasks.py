import random
import time
import threading


queue = []
MAX_ITEMS = 10

condition = threading.Condition()


class ProducerThread(threading.Thread):
    def run(self):
        numbers = range(5)
        global queue

        while True:
            condition.acquire()
            if len(queue) == MAX_ITEMS:
                print("Queue is full, producer is waiting")
                condition.wait()
                print("Space in queue, Consumer notified producer")
            number = random.choice(numbers)
            queue.append(number)
            print("Produced {}".format(number))
            condition.notify()
            condition.release()
            time.sleep(random.random())


class ConsumerThread(threading.Thread):
    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Nothing in queue, Consumer is waiting")
                condition.wait()
                print("Producer added something to the queue and notified the consumer")

            number = queue.pop(0)
            print("consumed {}".format(number))
            condition.release()
            time.sleep(random.random())


producer = ProducerThread()
producer.daemon = True
producer.start()

consumer = ConsumerThread()
consumer.daemon = True
consumer.start()

while True:
    time.sleep(1)