#!/usr/bin/env python3
""" script provides stats on nginx logs """
from pymongo import MongoClient


def nginx_logs_stats():
    """ connect to mongo """
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"] 
    for method in methods:
        count = collection.count_documents({"method": method})
    count_status = collection.count_documents({"method": "GET", "path": "/status"})
    client.close()
    nginx_logs_stats()
