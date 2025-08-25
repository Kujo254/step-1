class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

    @classmethod
    def get_population(cls):
        return cls.population


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying")

    @staticmethod
    def is_adult(age):
        return age >= 18

    @classmethod
    def from_string(cls, data_string):
        name, age, student_id = data_string.split(",")
        return cls(name, int(age), student_id)


class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


S1 = Student("Ali", 20, 900)
S2 = Student("Sara", 25, 901)
T1 = Teacher("Henry", 28, "Kiswahili")
S3 = Student.from_string("Josh,56,902")

S1.introduce()
S1.study()

S2.introduce()
S2.study()

T1.introduce()
T1.teach()

S3.introduce()
S3.study()

print("Is S1 an adult?", Student.is_adult(S1.age))
print("Current population:", Person.get_population())

print("\nInstance Attributes:")
print("S1 name:", S1.name)
print("S1 age:", S1.age)
print("S1 student_id:", S1.student_id)

print("\nClass Attribute:")
print("Population (via class):", Person.population)
print("Population (via instance):", S1.population)
