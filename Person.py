class Person:
    def __init__(self,
                 name=None,
                 gender=None,
                 age=None):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self):
        val = input("Input name:")
        self.name = val

    def get_gender(self):
        return self.gender

    def set_gender(self):
        val = input("Input gender:")
        self.gender = val

    def get_age(self):
        return self.age

    def set_age(self):
        val = input("Input age:")
        try:
            val = int(val)
            self.age = val
        except:
            raise ValueError("Age must be integer!")

    def display(self):
        print(f"{self.get_name()}, {self.get_gender()}, {self.get_age()}")
