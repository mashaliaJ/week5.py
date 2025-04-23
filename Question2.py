class Vehicle:
    def __init__(self, name, speed, color):
        self._name = name
        self._speed = speed 
        self._color = color
        self._is_moving = False
        self._fuel = 100

    def move(self):
        self._is_moving = True
        self._fuel -= 10
        print(f"{self._name} is moving at {self._speed} km/h")
    
    def stop(self):
        self._is_moving = False
        print(f"{self._name} has stopped")

    def honk(self):
        print(f"{self._name} goes HONK HONK!")
        
    def get_status(self):
        status = "moving" if self._is_moving else "stopped"
        return f"{self._color} {self._name} is {status}. Fuel: {self._fuel}%"


class Car(Vehicle):
    def __init__(self, name, speed, color, model):
        super().__init__(name, speed, color)
        self._model = model
        self._trunk_open = False

    def open_trunk(self):
        self._trunk_open = True
        print(f"{self._name}'s trunk is now open")
        
    def close_trunk(self):
        self._trunk_open = False
        print(f"{self._name}'s trunk is now closed")


class Motorcycle(Vehicle):
    def __init__(self, name, speed, color, type):
        super().__init__(name, speed, color)
        self._type = type
        self._stand_down = True

    def wheelie(self):
        if self._is_moving:
            print(f"{self._name} performs a wheelie!")
        else:
            print("Cannot do wheelie while stopped")
            
    def kick_stand(self, up=True):
        self._stand_down = not up
        position = "up" if up else "down"
        print(f"Kick stand {position}")


# Example usage:
car = Car("Civic", 180, "Blue", "Sedan")
bike = Motorcycle("Ninja", 250, "Red", "Sport")

car.move()
car.honk()
print(car.get_status())
car.open_trunk()
car.stop()

bike.kick_stand(up=True)
bike.move() 
bike.wheelie()
print(bike.get_status())
bike.stop()