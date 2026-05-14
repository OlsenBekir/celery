from fastapi import FastAPI
from pydantic import BaseModel
from tasks import save_message_async
from search import search_melding
from database import jobs_collection

app = FastAPI()

class Melding(BaseModel):
    melding: str

@app.post("/melding_async")
def create_melding_async(melding: Melding):
    task = save_message_async.delay(melding.melding)
    return {"status": "queued", "task_id": task.id}

@app.get("/jobs/{task_id}")
def job_status(task_id: str):
    job = jobs_collection.find_one({"task_id": task_id})
    if not job:
        return {"status": "not_found"}
    return {"task_id": task_id, "status": job["status"]}

@app.get("/search")
def search(q: str):
    return search_melding(q)

