from pprint import pprint

def build_car_list():
    car_list = []

    # Read valid car IDs and models from car-ids.txt file
    car_ids_and_models = {}
    with open('C:\\Users\\f9xuyp3\python-3\\files\\car-ids.txt', 'r') as ids_file:
        for line in ids_file:
            car_id, model = line.strip().split(', ')
            car_ids_and_models[int(car_id)] = model

    # Read car details from input.txt and filter out outliers
    with open('C:\\Users\\f9xuyp3\python-3\\files\\input.txt', 'r') as input_file:
        next(input_file)  # Skip the header line
        for line in input_file:
            car_id, mileage = line.strip().split(', ')
            car_id = int(car_id)
            mileage = float(mileage)
            if car_id in car_ids_and_models and mileage.is_integer():
                car_list.append({'id': car_id, 'miles': int(mileage), 'model': car_ids_and_models[car_id]})

    return car_list


def ex5():
    car_list = build_car_list()
    pprint(car_list)

ex5()
