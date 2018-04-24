class Person:

    # Tham số age và gender có giá trị mặc định.
    def __init__(self, name, age=1, gender="57"):
        self.name = name
        self.age = age
        self.gender = gender

    def showInfo(self):
        print("Ten: ", self.name)
        print("Nam Sinh: ", self.age)
        print("Khoa: ", self.gender)