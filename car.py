class Car:
    def __init__(
            self,
            brand,
            model,
            fuel_consumption,
            registry_number,
            price_per_hour,
            price_per_day,
            price_per_week):
        self.brand = brand
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.registry_number = registry_number
        self.price_per_hour = price_per_hour
        self.price_per_day = price_per_day
        self.price_per_week = price_per_week

    def __repr__(self):
        return f'{ self.brand } {self.model}, with registry number: {self.registry_number} and fuel consumption: ' \
               f'{self.fuel_consumption} L, price per: {self.price_per_hour}/h, {self.price_per_day}/d, ' \
               f'{self.price_per_week}/w.'
