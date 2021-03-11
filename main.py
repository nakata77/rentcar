from carFactory import CarFactory
from order import Order


def str_to_bool(v):
    return v.lower() in ("yes", "true", "t", "1")


car_list = CarFactory.create_car_collection('cars.json')
stop = False

while True:
    print("Select car/s for renting:")
    current_customer_orders = []
    selected_cars = []
    customer_invoice = 0

    for index, car in enumerate(car_list):
        print(f'{index + 1}: {car}')

    while True:
        car_index = input("Car index: ")
        rent_type = input("Rent type: ")
        rent_duration = ""
        if rent_type == "h":
            rent_duration = input("Rent duration: ")

        order = Order(car_index, rent_type, rent_duration)
        current_customer_orders.append(order)
        selected_cars.append(int(car_index))

        if len(car_list) == len(selected_cars):
            break

        chose_again = input("Do you want to rent another car: (True/False) ")

        if not str_to_bool(chose_again):
            break

    if len(selected_cars) > len(set(selected_cars)):
        print('Order contains duplicate selections')
        break

    for order in current_customer_orders:
        car = object
        car_id_catalog = int(order.car_id) - 1

        try:
            car = car_list[car_id_catalog]
        except IndexError:
            print(f'Car with index {car_id_catalog} is not present in the catalog!')

        if order.rent_type == 'h':
            customer_invoice += int(car.price_per_hour) * int(order.rent_duration)
        elif order.rent_type == 'd':
            customer_invoice += int(car.price_per_day)
        elif order.rent_type == 'w':
            customer_invoice += int(car.price_per_week)
        else:
            print("Invalid rent type")

    if len(selected_cars) >= 3:
        customer_invoice *= 0.7

    print(f'Final cost: {customer_invoice}')

    selected_cars.sort(reverse=True)
    for sc in selected_cars:
        del car_list[sc-1]

    if not car_list:
        break

    stop = input("Continue with next customer's order: (True/False)")
    if not str_to_bool(stop):
        break
