class Dog:
#This exercise is about creating a class in python.
#It is called whenever a Dog object is created.
# The reference called "self" is created by Python and made to point to the space for the newly created object.
# Python does this automatically for us but we have to have "self"
# as the first parameter to the __init__ method (i.e. the constructor).

    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
# This is an accessor method that returns the speakText stored in the
# object. Notice that "self" is a parameter. Every method has "self" as its # first parameter. The "self" parameter is a reference to the current
# object. The current object appears on the left hand side of the dot (i.e. # the .) when the method is called.
    def speak(self):
        return self.speakText

    def getName(self):
        return self.name

    def birthDate(self):
        return str(self.month) + '/' + str(self.day) + '/' + str(self.year)

    def changeBark(self, bark):
        self.speakText = bark
# When creating the new puppy we don’t know it’s birthday. Pick the
# first dog’s birthday plus one year. The speakText will be the
# concatenation of both dog’s text. The dog on the left side of the + # operator is the object referenced by the "self" parameter. The
# "otherDog" parameter is the dog on the right side of the + operator.
    def __add__(self, otherDog):
        return Dog('Puppy of ' + self.name +
                   ' and ' + otherDog.name, self.month, self.day, self.year + 1,
                   self.speakText + otherDog.speakText)

def main():
        dog1 = Dog('Mesa', 5,15,2014, 'woooof')
        dog2 = Dog('lily', 5,3,2016, 'barkbark')
        print(dog1.speak())
        print(dog2.speak())
        print(dog1. birthDate())
        print(dog2.birthDate())
        dog1.changeBark('woooofy')
        print(dog1.speak())
        puppy = dog1 + dog2
        print(puppy.speak())
        print(puppy.getName())
        print(puppy.birthDate())

if __name__ == '__main__':
          main()