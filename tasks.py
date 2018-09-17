import time
import threading


def countdown(count):
    while count >= 0:
        print("Count down {}".format(count))
        count -= 1
        time.sleep(1)

t1 = threading.Thread(name='countdown', args=(10,), target=countdown)
t1.start()

print("complete")
