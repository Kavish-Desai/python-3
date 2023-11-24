from ValidationException import ValidationException


def validate_file(myFile):
    try:
        with open(myFile, 'r') as file:
            lines = file.readlines()
            for line in lines:
                car_details = line.strip().split(',')
    
                car_name, mileage = car_details
                try:
                    int_mileage = int(mileage)
                except ValueError:
                    raise ValidationException(f"Invalid mileage value '{mileage}' for car '{car_name}'. Mileage should be a valid integer.")
    except FileNotFoundError:
        raise ValidationException(f"File '{myFile}' not found.")
    

def ex1():
    try:
        validate_file("C:\\Users\\f9xuyp3\python-3\\files\\input.txt")
    except ValidationException as ve:
        print(ve)

ex1()
