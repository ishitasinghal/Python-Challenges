class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self, fname, lname)
        self.graduationyear = year
    #
    # class DerivedClass(BaseClass):  # don't forget to declare inheritance
    #     def __init__(self, rank, *args,
    #                  **kwargs):  # in args, kwargs, there will be all parameters you don't care, but needed for baseClass
    #         super(DerivedClass, self).__init__(*args, **kwargs)
    #         self.rank = rank

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
# x = Person("John", "Doe")
# x.printname()

x = Student("Mike", "Olsen", 2019)
x.welcome()


# class Student(Person, object):
#     def __init__(self, firstName, lastName, idNumber, scores):
#         super().__init__(firstName, lastName, idNumber)
#         self.scores = scores
#     def calculate(self):
#         iAvg = sum(self.scores)/len(self.scores)
#         return 'O' if iAvg > 89 else 'E' if iAvg > 79 else 'A' if iAvg > 69 else 'P' if iAvg > 54 else 'D' if iAvg > 39 else 'T'