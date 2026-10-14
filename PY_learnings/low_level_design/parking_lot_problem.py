"""

"""

from abc import ABC, abstractmethod
from enum import Enum
from datetime import datetime


# Define the VehicleType enum
class VehicleType(Enum):
    CAR = 1
    MOTORCYCLE = 2
    EV = 3


class SpotType(Enum):
    COMPACT = 1
    LARGE = 2
    HANDICAPPED = 3
    ELECTRIC = 4


class Vehicle(ABC):
    def __init__(self, license_plate: str, vehicle_type: VehicleType):
        self.license_plate = license_plate
        self.vehicle_type = vehicle_type

    @abstractmethod
    def get_required_spot_type(self) -> SpotType:
        pass


class Car(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.CAR)

    def get_required_spot_type(self) -> SpotType:
        return SpotType.COMPACT


class Motorcycle(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.MOTORCYCLE)

    def get_required_spot_type(self) -> SpotType:
        return SpotType.COMPACT


class EV(Vehicle):
    def __init__(self, license_plate: str):
        super().__init__(license_plate, VehicleType.EV)

    def get_required_spot_type(self) -> SpotType:
        return SpotType.ELECTRIC


class ParkingSpot:
    def __init__(self, spot_id: str, spot_type: SpotType):
        self.spot_id = spot_id
        self.spot_type = spot_type
        self.is_occupied = False
        self.vehicle: Vehicle | None = None

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        if not self.is_occupied and vehicle.get_required_spot_type() == self.spot_type:
            self.vehicle = vehicle
            self.is_occupied = True
            return True
        return False

    def remove_vehicle(self) -> bool:
        if self.is_occupied:
            self.vehicle = None
            self.is_occupied = False
            return True
        return False


class ParkingFloor:
    def __init__(self, floor_id: str):
        self.floor_id = floor_id
        self.spots: list[ParkingSpot] = []

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle: Vehicle) -> ParkingSpot | None:
        for spot in self.spots:
            if not spot.is_occupied and vehicle.get_required_spot_type() == spot.spot_type:
                return spot
        return None


class ParkingLot:
    def __init__(self, lot_id: str):
        self.lot_id = lot_id
        self.floors: list[ParkingFloor] = []

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot and spot.park_vehicle(vehicle):
                print(f"Vehicle {vehicle.license_plate} parked at spot {spot.spot_id} on floor {floor.floor_id}.")
                return True
        print(f"No available spot for vehicle {vehicle.license_plate}.")
        return False

    def remove_vehicle(self, license_plate: str) -> bool:
        for floor in self.floors:
            for spot in floor.spots:
                if spot.is_occupied and spot.vehicle.license_plate == license_plate:
                    spot.remove_vehicle()
                    print(f"Vehicle {license_plate} removed from spot {spot.spot_id} on floor {floor.floor_id}.")
                    return True
        print(f"Vehicle {license_plate} not found in the parking lot.")
        return False


# example usage:
if __name__ == "__main__":
    # Create a parking lot
    parking_lot = ParkingLot("Lot1")

    # Create floors
    floor1 = ParkingFloor("Floor1")
    floor2 = ParkingFloor("Floor2")

    # Add spots to floors
    floor1.add_spot(ParkingSpot("F1S1", SpotType.COMPACT))
    floor1.add_spot(ParkingSpot("F1S2", SpotType.LARGE))
    floor2.add_spot(ParkingSpot("F2S1", SpotType.ELECTRIC))
    floor2.add_spot(ParkingSpot("F2S2", SpotType.HANDICAPPED))

    # Add floors to parking lot
    parking_lot.add_floor(floor1)
    parking_lot.add_floor(floor2)

    # Create vehicles
    car = Car("ABC123")
    motorcycle = Motorcycle("XYZ789")
    ev = EV("EV456")

    # Park vehicles
    parking_lot.park_vehicle(car)
    parking_lot.park_vehicle(motorcycle)
    parking_lot.park_vehicle(ev)

    # Remove a vehicle
    parking_lot.remove_vehicle("ABC123")


