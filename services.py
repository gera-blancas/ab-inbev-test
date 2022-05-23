from mongo import conectionDb
from utils import JSONEncoder
import json
from flask import request
import logging

def registerRoutes(app):
    @app.route("/")
    def start():
        return {
            "name": "Gerardo Blancas Hernandez",
            "app": "test"
        }

    @app.route("/search", methods=["GET"])
    def search():
        requestArgs = request.args
        return searchScore(request=requestArgs).score()


class searchScore():
    def __init__(self, request):
        self.q = request["q"]
        self.latitude = request["latitude"]
        self.longitude = request["longitude"]

    def score(self):
        if self.q and self.latitude and self.longitude:
            conection = conectionDb("test")
            query = { "$text": { "$search": self.q } }
            cities = json.loads(
                JSONEncoder().encode(
                    [i for i in conection.findCities(query=query)]
                    )
                )
            cities = self.calculateLongLat(float(self.latitude), float(self.longitude), cities)
            respose = {
                "status": 0,
                "response": cities
            }
            return respose, 200
        else:
            logging.error("One or more parameters of the request are empty")
            return {
                "status": -1,
                "message": "One or more parameters of the request are empty"
            }, 400
    
    def calculateLongLat(self, latitude, longitude , data):
        logging.info("Scoring the result")
        cities = []
        longitude *= -1 
        for city in data:
            latitudeCity = float(city["lat"])
            longitudeCity = float(city["long"])
            score = float(city["score"])

            latScore = abs(round(abs(latitudeCity - latitude) / latitude, 3) - 1)

            longScore = abs(round(abs(longitudeCity - (longitude)) / longitude, 3) - 1)

            score = round((score * 0.40) + (latScore * 0.30) + (longScore * 0.30), 3)

            cities.append(
                {
                    "name": city["name"],
                    "latitude": city["lat"],
                    "longitude": city["long"],
                    "score": score
                }
            )

        return sorted(cities, key=lambda d: d['score'], reverse=True) 
 