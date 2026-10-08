
class TemperatureSensor:
    def __init__(self, location, temperature):
        self.location = location
        self.temperature = temperature

    def increase_temperature(self):
        self.temperature += 1

    def decrease_temperature(self):
        self.temperature -= 1

    def show_temperature(self):
        print(f"{self.location}: {self.temperature} degrees")


# Skapa två sensorer
sensor1 = TemperatureSensor("Kitchen", 20)
sensor2 = TemperatureSensor("Bedroom", 18)

# Visa temperaturerna från början
sensor1.show_temperature()
sensor2.show_temperature()

# Öka temperaturen i Kitchen två gånger
sensor1.increase_temperature()
sensor1.increase_temperature()

# Minska temperaturen i Bedroom en gång
sensor2.decrease_temperature()

# Visa de nya temperaturerna
sensor1.show_temperature()
sensor2.show_temperature()
