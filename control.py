from machine import Pin

class Led:
    def __init__(self, pinNum):
        self.pinNum = pinNum
        self.pin = Pin(pinNum, Pin.OUT)
        self.pin.value(0)

    def get_value(self):
        return self.pin.value()
    
    def toggle(self):
        self.pin.value(not self.get_value())

    def TurnOn(self):
        self.pin.value(1)

    def TurnOff(self):
        self.pin.value(0)
    