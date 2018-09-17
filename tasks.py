import time
from datetime import timedelta

import redis

from celery import Celery
from celery.decorators import periodic_task
from celery.schedules import crontab

app = Celery('tasks', backend='redis://localhost:6379', broker='redis://localhost:6379')


@app.task(name='tasks.add')
def add(x, y):
    total = x + y
    print("{} + {} = {}".format(x, y, total))
    time.sleep(10)
    return total

def backoff(attempts):
    """
    increase time between retries waiting for process to heal
    :param attempts:
    :return:
    """
    return 2 ** attempts


@app.task(bind=True, max_retries=4)
def data_extractor(self):
    try:
        for i in range(1, 11):
            print("Found valid value! {}".format(i))
            if i == 5:
                raise ValueError("Index Error")
    except Exception as e:
        print("There was an exception let's retry after 5 seconds")
        # countdown = sec to wait before retry
        raise self.retry(exc=e, countdown=backoff(self.request.retries))


key = "thisisasomewhatrandomstringbutnotreally"


# run periodic task using celery beat, interval set by run_every
@periodic_task(bind=True, run_every=timedelta(seconds=3), name="tasks.send_mail_from_queue")
def send_mail_from_queue(self):
    REDIS_CLIENT = redis.Redis()
    timeout = 60 * 5
    have_lock = False
    my_lock = REDIS_CLIENT.lock(key, timeout=timeout)
    try:
        # Set critical path to be mutually exclusive to not grab the same "message" over and over again
        have_lock = my_lock.acquire(blocking=False)
        if have_lock:
            messages_sent = "example.mail"
            print("{} Email message successfully sent [{}]".format(self.request.hostname, messages_sent))
            # this is a placeholder to similuate a program taking time to do something
            time.sleep(3)
    finally:
        print("release resources")
        if have_lock:
            my_lock.release()
