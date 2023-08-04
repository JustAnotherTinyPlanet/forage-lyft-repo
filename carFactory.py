from car import Car
from battery.nubbinBattery import NubbinBattery
from battery.spindlerBattery import SpindlerBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class CarFactory:
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tires): 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tires)
        car = Car(engine, battery, tire)
        return car
    
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tires): 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = OctoprimeTire(tires)
        car = Car(engine, battery, tire)
        return car
    
    def create_palindrome(current_date, last_service_date,  warning_light_is_on, tires): 
        engine = SternmanEngine(warning_light_is_on)
        battery = SpindlerBattery(last_service_date, current_date)
        tire = CarriganTire(tires)
        car = Car(engine, battery, tire)
        return car

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, tires): 
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(tires)
        car = Car(engine, battery, tire)
        return car
    
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tires): 
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(tires)
        car = Car(engine, battery, tire)
        return car
    