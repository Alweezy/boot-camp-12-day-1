class Car(object):
    #setting some default values
    num_of_doors = 4
    num_of_wheels = 4
    def __init__(self, car_name='General', car_model='GM', car_type='saloon', car_speed=0):
        self.car_name = car_name
        self.car_model = car_model
        self.car_type = car_type
        self.car_speed = car_speed
        if self.car_name is 'Porshe' or self.car_name is 'Koenigsegg':
            self.num_of_doors = 2
        elif self.car_type is 'trailer':
            self.num_of_wheels = 8
        else:
            self

    def is_saloon(self):
        '''
            Determine between saloon and trailer
        '''
        if self.car_type is not 'trailer':
            return True
        return False

    def drive(self, car_speed):
        '''
            Check the car type and return appropriate speed
        '''
        if self.car_type is 'trailer':
            self.car_speed = car_speed * 11
        else:
            self.car_speed = 10 ** car_speed
        return self