from functools import reduce
from time import sleep
from typing import List
from data_management import db_count, db_insert, db_find_last_entry
from fastapi import FastAPI
import uvicorn

from tasks import sleep_task

app = FastAPI()


@app.get("/")
def index():
    return {"Message": "Hello"}


@app.get("/calculate/{a}/{b}")
def addition(a: int, b: int) -> int:
    return a + b


@app.get("/calculate")
def addition_query(a: int, b: int) -> int:
    return a + b


@app.post("/calculate/array")
def addition_array(int_list: List[int]) -> int:
    return reduce(lambda x, y: x + y, int_list)


@app.get("/sleep")
async def sleep(duration: int):
    sleep_task.delay(duration)
    return "ok"

@app.get("/last_entry")
async def last_sleep():
    return db_find_last_entry("Sleeping")

@app.get("/sleepy")
async def sleepy():
    return db_count("Sleeping")
