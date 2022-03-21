from .dataClass import Person
import JSONparser


save_file_JSON = "persons.json"

def newPerson():

       inputPersNr = int(input("PersonNr: "))
       inputFirstName = input("F Name: ")
       inputLastName = input("L Name: ")
       inputAge = int(input("Age: "))
       inputSalary = float(input("Salary: "))

       person = Person(inputPersNr,inputFirstName,inputLastName,inputAge,inputSalary)
       person = JSONparser.toString(person)
       personList = JSONparser.addPerson(person, save_file_JSON)
       JSONparser.saveList(personList, save_file_JSON)
       
    

def main():
    newPerson()

main()

    



















