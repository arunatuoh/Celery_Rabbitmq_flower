from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost:5672')

@app.task
def add(x, y):
    return x + y

# install rabbitmq server: sudo apt-get install rabbitmq-server
# check rabbitmq server: sudo rabbitmqctl status (sudo systemctl status rabbitmq-server)
# then enable rabbitmq server: sudo systemctl enable rabbitmq-server
# for UI management: rabbitmq-plugins enable rabbitmq_management
# run celery tasks: celery -A tasks worker --loglevel=info
# run flower: celery -A tasks flower --broker=pyamqp://guest@localhost:5672

# then try this
# envarun@arun-Latitude-5410:~/celery_example$ python
# Python 3.10.12 (main, Nov  6 2024, 20:22:13) [GCC 11.4.0] on linux
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from tasks import add
# >>> add.delay(4,5)
# <AsyncResult: 95fd2501-9739-4abd-b80c-6421e2f2876f>

# we can check on flower UI Task will come