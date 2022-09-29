from abc import ABC, abstractmethod

class Bakeable(ABC):
    @abstractmethod
    def bake(self):
        pass

class Bread(Bakeable):
    def bake(self):
        print("baking bread")

class Cookie(Bakeable):
    def bake(self):
        print("baking cookie")

def cook(bakeable: Bakeable):
    bakeable.bake()

if __name__ == "__main__":
    cookie = Cookie()
    bread = Bread()
    cook(cookie)
    cook(bread)
