from elasticsearch import Elasticsearch


es = Elasticsearch("http://localhost:9200")


def create_index(index_name):
    if es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)
    es.indices.create(index=index_name, body={
        "mappings": {
            "properties": {
                "department": {"type": "keyword"},
                "threat_score": {"type": "integer"}
            }
        }
    })
    print(f"Index '{index_name}' created.")


def upload_to_elasticsearch(data, index_name):
    for _, row in data.iterrows():
        es.index(index=index_name, body=row.to_dict())
    print(f"Data uploaded to index '{index_name}'.")


def calculate_aggregated_threat_score(index_name):
    query = {
        "size": 0,
        "aggs": {
            "overall_score": {
                "avg": {
                    "field": "threat_score"
                }
            },
            "by_department": {
                "terms": {"field": "department"},
                "aggs": {
                    "avg_score": {"avg": {"field": "threat_score"}}
                }
            }
        }
    }
    response = es.search(index=index_name, body=query)
    overall_score = response["aggregations"]["overall_score"]["value"]
    department_scores = response["aggregations"]["by_department"]["buckets"]

    return overall_score, department_scores
