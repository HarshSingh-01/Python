class vehicle(object):
    def __init__(self,Modelname,color,maxspeed):
        self.Modelname = Modelname
        self.color = color 
        self.maxspeed = maxspeed
        
    def speedchanger(self):
        a = (self.maxspeed/18)*5
        print("Speed in m/sec:",a)
        
    def tankFull(self):
        print(self.Modelname,"tank is full")
        
    def tankEmpty(self):
        print(self.Modelname,"tank is Empty")
    
    def maintainance(self,maintainance):
        print(self.Modelname,"maintaince after",maintainance,"months")


class car(vehicle):
    def __init__(self,Modelname,color,maxspeed):
        super().__init__(Modelname,color,maxspeed)
    
    def hornsound(self):
        print("Beep beep!")
        
class truck(vehicle):
    def __init__(self,Modelname,color,maxspeed):
        super().__init__(Modelname,color,maxspeed)
    
    def hornsound(self):
        print("Horn!")
    
vehicle = car("Mercedes","silver",400)
vehicle.maintainance(6)