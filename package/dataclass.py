import helpers
from operator import itemgetter

class Person:
    def __init__(self, persId, firstName, lastName, age, salaray):
        self.persId = persId
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salaray = salaray 

    def printPerson(self):
        print("{0:04d} {1:20s} {2:20s} {3} {4:8.2f}".format(self.persId, self.firstName, self.lastName, self.age, self.salaray))
    
def createPerson(): 
    inputPersId = int(input("PersonId: "))
    inputFirstName = input("F Name: ")
    inputLastName = input("L Name: ")
    inputAge = int(input("Age: "))
    inputSalary = float(input("Salary: "))

    person = Person(inputPersId, inputFirstName, inputLastName, inputAge, inputSalary)
    return person

def newPerson(saveFile):
    person = createPerson()
    personStr = helpers.toString(person)
    personList = helpers.addPerson(personStr, saveFile)
    helpers.saveList(personList, saveFile) 

def listAllPersons(jsonFile):
    personList = helpers.getList(jsonFile)
    personList.sort(key=itemgetter("persId"), reverse=True)
    print(personList)


