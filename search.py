from es_client import es

def search_melding(query: str):
    response = es.search(
        index="meldinger",
        query={"match": {"melding": query}}
    )

    results = []
    for hit in response["hits"]["hits"]:
        results.append({
            "score": hit["_score"],
            "melding": hit["_source"]["melding"]
        })

    return results
