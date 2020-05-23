import csv


class CarBase:

    # todo too many arguments passed
    def __init__(self, car_type, photo_file_name, brand, carrying):
        if type(car_type) != str:
            raise TypeError('car_type is not recognized')
        if type(photo_file_name) != str:
            raise TypeError('photo_file_name is not recognized')
        # if photo_file_name.find('.') == -1:
        #     raise TypeError('photo_file_name does not have proper format')
        if type(brand) != str:
            raise TypeError('brand is not recognized')
        # todo check what should carrying store
        # if type() != str:
        #     raise TypeError('car_type is not recognized')
        self.car_type = car_type
        self.photo_file_name = photo_file_name
        self.brand = brand
        self.carrying = carrying


class Car(CarBase):
    def __init__(self, car_brand, photo_file_name, carrying, passenger_seats_count ):
        try:
            super().__init__(type(self).__name__, photo_file_name, car_brand, carrying)
            self.passenger_seats_count = passenger_seats_count
        except TypeError as err:
            print("Type error occurred: ", err)


class Truck(CarBase):
    def __init__(self, car_brand, photo_file_name, carrying, body_whl):
        try:
            super().__init__(type(self).__name__, photo_file_name, car_brand, carrying)
            self.__parse_whl(body_whl)
        except TypeError as err:
            print("Type error occurred: ", err)

    def __parse_whl(self, body_whl):
        body_whl_arr = body_whl.split('x')
        if len(body_whl_arr) != 3:
            raise TypeError('Incorrect WxHxl passed: ', body_whl)
        self.body_width = body_whl_arr[0]
        self.body_height = body_whl_arr[1]
        self.body_length = body_whl_arr[2]

    def get_body_volume(self):
        return self.carrying


class SpecMachine(CarBase):
    def __init__(self, car_brand, photo_file_name, carrying, extra):
        try:
            super().__init__(type(self).__name__, photo_file_name, car_brand, carrying)
            self.extra = extra
        except TypeError as err:
            print("Type error occurred: ", err)


def get_car_list(file_name):
    car_list = []
    try:
        with open(file_name, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            next(reader)
            for row in reader:
                car_type = row[0]
                car_obj = None
                if car_type == 'car':
                    car_obj = Car(row[1], row[3], row[5], row[2])
                elif car_type == 'truck':
                    car_obj = Truck(row[1], row[3], row[5], row[4])
                elif car_type == 'spec_machine':
                    car_obj = SpecMachine(row[1], row[3], row[5], row[6])
                if car_obj:
                    car_list.append(car_obj)
    except (AttributeError, IndexError) as err:
        print('Attr Index ', err)
    # todo check what is the difference between these file errors below
    except (FileExistsError, FileNotFoundError) as err:
        print('Some problems with files: ', err)

    return car_list
