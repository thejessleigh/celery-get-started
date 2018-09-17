import time

def countdown(count):
    while count >= 0:
        print("Count down {}".format(count))
        count -= 1
        time.sleep(1)

countdown(10)
print("complete")