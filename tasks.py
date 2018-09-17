from celery import Celery

app = Celery('tasks', backend=None, broker='redis://localhost:6379')


@app.task(name='tasks.add')
def add(x, y):
    print("{} + {} = {}".format(x, y, x + y))
