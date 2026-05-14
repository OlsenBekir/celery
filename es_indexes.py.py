from es_client import es

def create_es_index():
    body = {
        "settings": {
            "analysis": {
                "analyzer": {
                    "default": {"type": "standard"}
                }
            }
        },
        "mappings": {
            "properties": {
                "melding": {"type": "text"},
                "created_at": {"type": "date"}
            }
        }
    }

    es.indices.create(index="meldinger", body=body, ignore=400)
    print("Elasticsearch index created.")

if __name__ == "__main__":
    create_es_index()
