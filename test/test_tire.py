import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tires = [0.1,0.3,0.4,0.9]
        carrigan = CarriganTire(tires)
        self.assertTrue(carrigan.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tires = [0.1,0.3,0.4,0.7]
        carrigan = CarriganTire(tires)
        self.assertFalse(carrigan.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tires = [0.7,0.6,0.8,0.9]
        octoprime = OctoprimeTire(tires)
        self.assertTrue(octoprime.needs_service())
    
    def test_tire_should_not_be_serviced(self):
        tires = [0.7,0.6,0.8,0.5]
        octoprime = OctoprimeTire(tires)
        self.assertFalse(octoprime.needs_service())