import threading

counter_buffer = 0
counter_lock = threading.Lock()

COUNTER_MAX = 100


def create_consumers(consumer_count):
    for i in range(consumer_count):
        t = threading.Thread(target=consumer_action)
        t.start()
        t.join()


def consumer_action():
    global counter_buffer
    for i in range(COUNTER_MAX):
        counter_lock.acquire()
        counter_buffer += 1
        counter_lock.release()


create_consumers(10)
print(counter_buffer)
