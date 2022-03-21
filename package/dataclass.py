class Person:
    def __init__(self, persId, firstName, lastName, age, salaray):
        self.persId = persId
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.salaray = salaray 

    def printPerson(self):
        print("{0:04d} {1:20s} {2:20s} {3} {4:8.2f}".format(self.persId, self.firstName, self.lastName, self.age, self.salaray))

#    def toJsonString(self):
#       jsonString = json.dumps(self.__dict__)
#       return jsonString
  
