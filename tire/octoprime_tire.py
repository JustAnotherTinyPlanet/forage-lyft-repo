from tire import Tire

class OctoprimeTire(Tire):
    def __init__(self,tires):
        self.tires = tires
    
    def needs_service(self):
        sum = 0
        for tire in self.tires:
            sum += tire
        return sum >= 3.0
