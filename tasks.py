import time

from celery import Celery

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
