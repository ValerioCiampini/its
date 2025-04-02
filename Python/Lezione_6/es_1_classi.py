class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

alice = Person("Alice W.", 45)
bob = Person("Bob M.", 36)

if alice.age > bob.age:
    print(alice)
else:
    print(bob)

erik = Person("Erik. B", 30)
james = Person("James .L", 26)
mary = Person("Mary .P", 32)

people:list = []

people.append(alice.age)
people.append(bob.age)
people.append(erik.age)
people.append(james.age)
people.append(mary.age)

min_:int = people[0]

for i in people:
    if i < min_:
        min_ = i
    
print(min_)