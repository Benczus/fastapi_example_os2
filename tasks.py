from time import sleep
from data_management import db_insert
from celery import Celery

tasks=Celery()


@tasks.task()
def sleep_task(duration):
    sleep(duration)
    db_insert({"Sleeping": duration})
    return