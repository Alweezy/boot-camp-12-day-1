class Car(object):
    car_doors=4
    car_wheels=4
    def __init__(self, car_name='General', car_model='GM', car_type='saloon', car_doors=4, car_wheels=4):
        self.__car_name = car_name
        self.__car_model = car_model
        self._car_doors = car_doors
        self.__car_type = car_type
        self._car_wheels = car_wheels
        self.speed = 0

    @property
    def name(self):
        return self.__car_name

    @property
    def model(self):
        return self.__car_model

    @property
    def num_of_doors(self):
        if self.__car_name in ['Koenigsegg', 'Porshe']:
            self._car_doors = 2
            return self._car_doors
        return self._car_doors

    @property
    def num_of_wheels(self):
        if self.__car_type is 'trailer':
            self._car_wheels = 8
            return self._car_wheels
        return self._car_wheels

    def is_saloon(self):
        if self.__car_type is 'saloon':
            return True
        return False

    @property
    def num_of_wheels(self):
        if self.__car_type is 'trailer':
            self._car_wheels = 8
            return self._car_wheels
        return self._car_wheels

    @property
    def type(self):
        return self.__car_type

    def drive(self,  drive_number):
        if self.type == 'trailer':
            if drive_number >= 1:
                self.speed = 77
                return self
            return self
        else:
            if drive_number >= 1:
                self.speed = 1000
                return self
            return self