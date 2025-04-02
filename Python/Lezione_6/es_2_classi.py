class Student:
    def __init__(self, name:str, studyprogram:str, age:int, gender:str):
        self.name = name
        self.studyprogram = studyprogram
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        print(f"{self.name}:{self.studyprogram}:{self.age}:{self.gender}")

erik = Student("Erik", "Economy", 21, "M")
mary = Student("Mary", "Politics", 23, "F")
james = Student("James", "Science", 22, "M")

erik.printInfo()
mary.printInfo()
james.printInfo()


