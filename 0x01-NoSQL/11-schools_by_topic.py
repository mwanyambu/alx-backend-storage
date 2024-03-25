#!/usr/bin/env python3
""" schools by tipic """


def schools_by_topic(mongo_collection, topic):
    """ filter topics"""
    return mongo_collection.find({"topics": topic})
