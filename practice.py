import redis
from celery import Celery
from celery.schedules import crontab
import random

r = redis.Redis(host="localhost",port=6379,db=0)

app = Celery(
    "practice",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

app.conf.beat_schedule = {
    "set-random-number-every-minut":{
        'task':"practice.set_random_number",
        'schedule':crontab(minute="*"),
    }
}


@app.task
def to_celery(number:int):
    result = number**2
    print(f"Result {number} ** 2 = {result}")
    if r.exists(f"number:{number}"):
        print(f"!!! {number} is exists")
        return result
    r.set(f"number:{number}",result)
    print('!!!saved!!!')
    return result

@app.task
def get_all_from_redis():
    keys = r.keys("number:*")
    print(keys)
    return keys

@app.task
def set_random_number():
    random_int = random.randint(0,1000)
    print(random_int)
    return to_celery(random_int)
    