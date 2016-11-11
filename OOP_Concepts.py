class Car(object):
    #setting some default values
    num_of_doors = 4
    num_of_wheels = 4
    def __init__(self, name='General', model='GM', car_type='saloon', speed=0):
        self.__name = name
        self.__model = model
        self.__car_type = car_type
        self.__speed = speed
        if self.name is 'Porshe' or self.name is 'Koenigsegg':
            self.__num_of_doors = 2
        elif self.__car_type is 'trailer':
            self.__num_of_wheels = 8
        else:
            self
    @property
    def is_saloon(self):
        '''
            Determine between saloon and trailer
        '''
        if self.car_type is not 'trailer':
            return True
        return False
    @property
    def drive(self, speed):
        '''
            Check the car type and return appropriate speed
        '''
        if self.__car_type is 'trailer':
            self.speed = speed * 11
        else:
            self.speed = 10 ** speed
        return self
