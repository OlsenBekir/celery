import time
from datetime import datetime
from celery_app import celery_app
from database import collection, jobs_collection
from es_client import es

@celery_app.task(queue="celery")
def save_message_async(melding: str):
    task_id = save_message_async.request.id

    jobs_collection.insert_one({
        "task_id": task_id,
        "status": "processing"
    })

    time.sleep(1)

    collection.insert_one({"melding": melding})

    es.index(
        index="meldinger",
        document={
            "melding": melding,
            "created_at": datetime.utcnow()
        }
    )

    jobs_collection.update_one(
        {"task_id": task_id},
        {"$set": {"status": "completed"}}
    )

    return "OK"

