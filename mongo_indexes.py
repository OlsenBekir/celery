from database import db

def create_indexes():
    db.jobs.create_index("task_id", unique=True)
    db.meldinger.create_index("melding")

if __name__ == "__main__":
    create_indexes()
    print("MongoDB indexes created.")
