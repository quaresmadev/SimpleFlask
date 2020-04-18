from flask_restful import Resource, reqparse, request
import json

class Carro(Resource):

    cars = [{
        "brand": "FORD",
        "model": "Mustang",
        "year": 2019
    }, {
        "brand": "FERRARI",
        "model": "F450",
        "year": 2020
    }]

    def get(self):  
        return self.cars, 200

    def post(self):   
        dados = json.loads(request.data)
        self.cars.append(dados)
        return self.cars
        
