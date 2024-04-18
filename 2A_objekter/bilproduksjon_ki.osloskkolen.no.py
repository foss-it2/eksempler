class Battery:
    def __init__(self, model_number: str, capacity: int):
        self.model_number = model_number
        self.capacity = capacity

    def charge(self):
        # Implementer ladelogikk her
        pass


class Car:
    def __init__(self, car_id: str, model_name: str, battery: Battery):
        self.id = car_id
        self.model_name = model_name
        self.battery = battery

    def get_id(self) -> str:
        return self.id

    def get_model_name(self) -> str:
        return self.model_name

    def get_battery(self) -> Battery:
        return self.battery


class StandardCar(Car):
    def __init__(self, car_id: str, model_name: str, battery: Battery):
        # Kall superklassens konstruktør
        super().__init__(car_id, model_name, battery)


class LuxuryCar(Car):
    extra_features = "Selvkjøring, luksuriøse interiørdetaljer"

    def __init__(self, car_id: str, model_name: str, battery: Battery):
        # Kall superklassens konstruktør
        super().__init__(car_id, model_name, battery)

    def get_extra_features(self) -> str:
        return self.extra_features


# Opprett et batteriobjekt
battery_60kwh = Battery("B-123", 60)
battery_100kwh = Battery("B-456", 100)
battery_120kwh = Battery("B-789", 120)

# Opprett bilene og legg dem til i produksjonssystemet
cars = ""
cars.append(StandardCar("C-001", "Standardmodell 1", battery_60kwh))
cars.append(LuxuryCar("C-002", "Luksusmodell 1", battery_120kwh))
cars.append(StandardCar("C-003", "Standardmodell 2", battery_100kwh))
cars.append(LuxuryCar("C-004", "Luksusmodell 2", battery_120kwh))

# Vis en oversikt over alle bilene i produksjonssystemet
for car in cars:
    print("Bil ID:", car.get_id())
    print("Modellnavn:", car.get_model_name())
    print("Batterikapasitet:", car.get_battery().capacity)
    if isinstance(car, LuxuryCar):
        print("Ekstrautstyr:", car.get_extra_features())
    print()

# Foreta et batteribytte på en bil
car_to_service = cars[0]
old_battery = car_to_service.get_battery()
new_battery = Battery("B-999", 80)

print("Batteribytte på bil", car_to_service.get_id())
print("Gammelt batteri:", old_battery.model_number,
      "- Kapasitet:", old_battery.capacity)
print("Nytt batteri:", new_battery.model_number,
      "- Kapasitet:", new_battery.capacity)

# Opprett en ny StandardCar-instans med det nye batteriet
new_standard_car = StandardCar(
    car_to_service.get_id(), car_to_service.get_model_name(), new_battery)
cars.remove(car_to_service)  # Fjern den gamle bilen fra produksjonssystemet
cars.append(new_standard_car)  # Legg til den nye bilen med det nye batteriet

print("Batteribytte fullført!")
print("Bil ID:", new_standard_car.get_id())
print("Nytt batteri:", new_standard_car.get_battery().model_number,
      "- Kapasitet:", new_standard_car.get_battery().capacity)
