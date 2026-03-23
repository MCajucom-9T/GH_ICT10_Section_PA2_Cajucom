# Object Oriented Programming
from pyscript import display, document


"""class Section: # creating the class
    def __init__(self, numstudents, name, level, adviser):
        self.numstudents = numstudents # attributes
        self.name = name # attributes
        self.level = level # attributes
        self.adviser = adviser # attributes


    #instantiating an object
section1 = Section(24, 'Topaz', 10, 'Mr. Cortez')
section2 = Section(25, 'Sapphire', 10, 'Mr. De Guzman')

display(f'{section1.level}-{section1.name} is part of Red Bulldogs', target='display1')
display(f'{section2.level}-{section2.name} is part of Yellow Tigers', target='display1')"""

def dog_info(e):
    class Dog: 
        def __init__(self, breed, age, name, owner):
            self.breed = breed
            self.age = age
            self.name = name
            self.owner = owner

        def bark(self):
            display('Arf'*3, target='display1')
        

    dog1 = Dog('Shih tzu', 16, 'Shino', 'Martina')
    dog2 = Dog('American Bully', 1, 'Mari', 'Skyler')
    dog1.bark()


    display(f'{dog1.name} is owned by {dog1.owner}', target='display1')

    # creating a child class
    class GermanShepard(Dog):
        pass

    dog1 = GermanShepard('German Shepard', 10, 'Jack', 'Simran')
    display(f'{dog1.name} is owned by {dog1.owner}', target='display1')

    class ShihTzu(Dog):
        pass 

    breed = document.getElementById("input1").value
    age = document.getElementById("input2").value
    name = document.getElementById("input3").value
    owner = document.getElementById("input4").value

    dog1 = ShihTzu(breed, age, name, owner)
    display(f'{dog1.name} is owned by {dog1.owner}', target='display1')
