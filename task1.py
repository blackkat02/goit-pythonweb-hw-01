from abc import ABC, abstractmethod
import logging

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(message)s')

class Vehicle(ABC):
    
    @abstractmethod
    def start_engine(self):
        pass

# ----- Конкретні класи продуктів -----
class Car(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region}): Двигун запущено.")

class Motorcycle(Vehicle):
    def __init__(self, make: str, model: str, region: str):
        self.make = make
        self.model = model
        self.region = region

    def start_engine(self):
        logging.info(f"{self.make} {self.model} ({self.region}): Мотор заведено.")

# ----- Абстрактна фабрика -----
class VehicleFactory(ABC):
    
    @abstractmethod
    def create_car(self, make: str, model: str) -> Car:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        pass

# ----- Конкретні фабрики -----
class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        logging.info(f"Створення автомобіля для США: {make} {model}")
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        logging.info(f"Створення мотоцикла для США: {make} {model}")
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Car:
        logging.info(f"Створення автомобіля для ЄС: {make} {model}")
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Motorcycle:
        logging.info(f"Створення мотоцикла для ЄС: {make} {model}")
        return Motorcycle(make, model, "EU Spec")

# ----- Використання -----
if __name__ == '__main__':
    us_factory = USVehicleFactory()
    us_car = us_factory.create_car("Ford", "Mustang")
    us_moto = us_factory.create_motorcycle("Harley-Davidson", "Sportster")

    eu_factory = EUVehicleFactory()
    eu_car = eu_factory.create_car("Volkswagen", "Golf")
    eu_moto = eu_factory.create_motorcycle("BMW", "R 1250 GS")

    vehicles = [us_car, us_moto, eu_car, eu_moto]
    for vehicle in vehicles:
        vehicle.start_engine()
