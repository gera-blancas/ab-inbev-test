from pymongo import MongoClient
import logging

class conectionDb():
    def __init__(self, dbName):
        self.dbName = dbName

        client = MongoClient("localhost", 27017)
        self.db = client[self.dbName]
        self.colectionCities = self.db["cities"]

    def findCities(self, query):
        logging.info("Finding the query in the data")
        return self.colectionCities.find(query, { "score": { "$meta": "textScore" } })
