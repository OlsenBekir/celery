from celery_app import celery_app
from database import collection
import time

@celery_app.task(queue="celery")
def save_message_async(melding: str):
    time.sleep(1)
    collection.insert_one({"melding":melding})
    return "OK"

