class Integer:
    value = 0
    def __init__(self, n):
        self.value = n
        
    def getValue(self):
        return self.value

x = Integer(7)
y = 7
z = x
#print(z)


class Vehicle:
    wheels = 0
    colour = ""
    make = ""
    year = 0
    def __init__(self, w, c, m, y):
        self.wheels = w
        self.colour = c
        self.make = m
        self.year = y
        
    def getWheels(self):
        return self.wheels
    
    def getColour(self):
        return self.colour
    
    def getMake(self):
        return self.make
    
    def getYear(self):
        return self.year
    
    
class Car(Vehicle):
    
    def __init__(self, c, m, y):
        Vehicle.__init__(self, 4, c, m, y)
            
class HondaCRV(Car):
    
    def __init__(self, c, y):
        Car.__init__(self, c, "Honda CR-V", y)
            
n = HondaCRV("Blue", "2005")
m = Car("Orange", "Tesla Roadster", 2020)
print(str(m.getWheels())+str(m.getColour()))
print(m.getMake())
print(m.getYear())
print(n.getWheels())
print(n.getColour())
print(n.getMake())
print(n.getYear())

class Organism:
    species = ""
    def __init__(self, spec):
        self.species = spec
        
    def getSpecies(self):
        return self.species
    
    def setSpecies(self, spec):
        self.species = spec


class Person(Organism):
    firstname = ""
    lastname = ""
    #father = Person("Jesus", "Christ")
    def __init__(self, first, last):
        Organism.__init__(self, "human")
        self.firstname = first
        self.lastname = last

    def getName(self):
        return self.firstname +" "+ self.lastname
    
    def changeFirstName(self, first):
        self.firstname = first




a = Person("Jesus", "Christ")
c = Person("Jenny", "Doe")
b = Organism("cat")
print(a.getSpecies())
print(b.getSpecies())

#print(x.getValue())
