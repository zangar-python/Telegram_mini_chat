from celery import Celery
from celery.schedules import crontab

app = Celery(
    "tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)
app.conf.beat_schedule = {
    "say-hello-every-minute":{
        "task":"tasks.hello",
        "schedule":crontab(minute="*")
    }
}

@app.task
def add(x,y):
    return x+y

@app.task
def hello():
    print("Hello,world!")