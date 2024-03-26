#!/usr/bin/env python3
""" script provides stats on nginx logs """
from pymongo import MongoClient


def nginx_logs_stats():
    """ connect to mongo """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    logs = collection.count_documents({})
    print(f"{logs} logs")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"    method {method}: {count}")
    count_status = collection.count_documents(
            {"method": "GET", "path": "/status"})
    print(f"{count_status} status check")
    client.close()


if __name__ == "__main__":
    nginx_logs_stats()
