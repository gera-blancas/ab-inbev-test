# ab-inbev-test
ab-inbev-test is a api REST that was developed by Gerardo Blancas. 

The language that this api is programming is python 3 with the framework Flask and use a data base no relational with the MongoDB engine. The performance of the api is to make a score according to the word, altitude and longitude that send in the request.

### Request

The method that the api use is a GET that send the next data in the request: 

>q: Text that you are looking for

>latitude: Latitud of the city

>longitude: Longitude of the city


### Response

The response that the api sends is:

>status: status code

>response: A list of result in descending score


The status code that the api uses are the next:

>0: correct

>-1: incorrect



### Examples


Example of a correct response:


Request:

>q:Bridgewater

>latitude:44.39

>longitude:-88.91

Response:

>{
    "response": [
        {
            "latitude": "40.60079",
            "longitude": "-74.64815",
            "name": "Bridgewater",
            "score": 0.927
        },
        {
            "latitude": "38.38207",
            "longitude": "-78.9767",
            "name": "Bridgewater",
            "score": 0.926
        },
        {
            "latitude": "41.99038",
            "longitude": "-70.97504",
            "name": "Bridgewater",
            "score": 0.923
        },
        {
            "latitude": "44.38345",
            "longitude": "-64.51546",
            "name": "Bridgewater",
            "score": 0.918
        },
        {
            "latitude": "42.01899",
            "longitude": "-71.00782",
            "name": "West Bridgewater",
            "score": 0.824
        },
        {
            "latitude": "42.03343",
            "longitude": "-70.95921",
            "name": "East Bridgewater",
            "score": 0.824
        }
    ],
    "status": 0
}



Example of response with no records found:


Request:

>q:SomeCity

>latitude:44.39

>longitude:-88.91


Response:

>{
    "response": [],
    "status": 0
}


Example of incorrect response:

Request:

>q:

>latitude:44.39

>longitude:-88.91


Response:

>{
    "message": "One or more parameters of the request are empty",
    "status": -1
}
