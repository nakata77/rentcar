import json

from car import Car


class CarFactory:
    @staticmethod
    def create_car_collection(json_path):
        car_list = []
        with open(json_path, 'r') as json_file:
            car_data = json.loads(json_file.read())
            for c in car_data:
                car_list.append(Car(**c))
            return car_list
