from fastapi import FastAPI
from pydantic import BaseModel
from tasks import save_message_async

app = FastAPI()

class Melding(BaseModel):
    melding: str

    @app.post("/melding_async")
    def create_melding_async(melding: Melding):
        task = save_message_async.delay(melding.melding)

        return{
            "status": "queued",
            "task_id": task.id
        }