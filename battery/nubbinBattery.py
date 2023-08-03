from battery import Battery
from dateCalculator import dateCalculator


def NubbinBattery(Battery):
    def __init__(self, last_service_date, current_date):
        self.last_service_date = last_service_date
        self.current_date = current_date
        
    def needs_service(self):
        return dateCalculator(self.last_service_date, self.current_Date) > 4
