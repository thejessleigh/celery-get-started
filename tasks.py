import time
import threading


def countdown(count):
    while count >= 0:
        print("{} Count down {}".format(threading.current_thread().name, count))
        count -= 1
        time.sleep(1)

def countup(count):
    while count <= 10:
        print("{} Count up {}".format(threading.current_thread().name, count))
        count += 1
        time.sleep(1)

t1 = threading.Thread(name='countdown', args=(10,), target=countdown)
t1.start()

t2 = threading.Thread(name='countdown', args=(0,), target=countup)
t2.start()

print("complete")
