class Car:
    def __init__(self,name, rent):
        self.name = name
        self.rent = rent


def accelerate(Car):
    Car.rent += 100

brz = Car("brz", 100)
lambo = Car("gallardo", 200)

accelerate(brz)
print(brz.name + " " + str(brz.rent))
print(lambo.rent)
