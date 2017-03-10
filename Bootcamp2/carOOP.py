class Car(object):

    num_of_doors = 4
    num_of_wheels = 4
    speed = 0

    def __init__(self, car_type, name='General', model='GM'):  #Defining default variables within the __init__
        self.name = name
        self.model = model
        self.car_type = car_type
        
    def num_of_doors(self): #method for finding number of doors
        if self.name == 'Porshe' or self.name == 'Koenigsegg':  
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4


    def num_of_wheels(self):

        if self.car_type == 'trailer':  
            self.num_of_wheels = 8
        else:
            self.num_of_wheels=4


    def is_saloon(self):  #method for finding car_type
        if self.car_type != 'Trailer':  
            self.car_type = 'Saloon'

        return self.car_type

    def drive(self, speed):  # function to calculate different car type speeds. 
        if self.car_type == 'trailer':
            self.speed = 77
        else:
            self.speed = pow(10, speed)
        return self.speed