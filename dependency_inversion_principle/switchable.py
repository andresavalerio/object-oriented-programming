from abc import ABC, abstractmethod

class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on")
    
    def turn_off(self):
        print("Fan: turned off")


class LightBulb(Switchable):
    def turn_on(self):
        print("Lightbulb: turned on")
    
    def turn_off(self):
        print("Lightbuld: turned off")


class PowerSwitch():
    def __init__(self, l: Switchable):
        self.switchable = l
        self.on = False
    
    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True


if __name__ == '__main__':
    hueBulb = LightBulb()
    switch = PowerSwitch(hueBulb)
    switch.press()
    switch.press()
    switch.press()
    switch.press()
    switch.press()

    badroomFan = Fan()
    switch = PowerSwitch(badroomFan)
    switch.press()
    switch.press()
    switch.press()
    switch.press()
    switch.press()