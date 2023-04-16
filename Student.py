from Human import Human
from Mark import Mark
from tabulate import tabulate
import csv
import os.path
import sys


class Student(Human):
    ls_student = []

    def __init__(self,
                 student_id=None,
                 name=None,
                 gender=None,
                 age=None,
                 mark=Mark(),
                 average_mark=0,
                 performance=None):
        super().__init__(name, gender, age)
        self.student_id = student_id
        self.mark = mark
        self.average_mark = average_mark
        self.performance = performance

    def get_student_id(self):
        return self.student_id

    def set_student_id(self, val):
        self.student_id = val

    def get_mark(self):
        return self.mark

    def set_mark(self):
        self.get_mark().set_math_mark()
        self.get_mark().set_physics_mark()
        self.get_mark().set_chemistry_mark()

    def set_average_mark(self, val):
        self.average_mark = val

    def get_performance(self):
        return self.capacity

    def set_performance(self, val):
        self.capacity = val

    def get_average_mark(self):
        ave_mark = self.get_mark().calc_ave_mark()
        self.set_average_mark(ave_mark)
        return self.average_mark

    def calc_performance(self):
        average_mark = self.get_average_mark()
        math_mark = self.get_mark().get_math_mark()
        physics_mark = self.get_mark().get_physics_mark()
        chemistry_mark = self.get_mark().get_chemistry_mark()
        if average_mark >= 8 and math_mark > 8 and physics_mark > 7 and chemistry_mark > 7:
            self.set_performance("Good")
        elif 6.5 <= average_mark < 8 and math_mark > 8 and physics_mark > 5 and chemistry_mark > 5:
            self.set_performance("Quite good")
        elif 5 <= average_mark < 6.5 and math_mark > 5 and physics_mark > 4 and chemistry_mark > 4:
            self.set_performance("Medium")
        elif average_mark < 5:
            self.set_performance("Bad")
        else:
            self.set_performance("Quite Good")

        return self.get_performance()

    @classmethod
    def read_from_file(cls, url_path='Student.csv', *agrs, **kwargs):
        """ Method to read list student from file csv """
        Student.ls_student = []
        if agrs:
            url_path = agrs[0]
        if os.path.exists(url_path):
            with open('Student.csv', **kwargs) as f:
                reader = csv.DictReader(f, delimiter=',')
                students = list(reader)
                i = 0
                for row in students:
                    mark = Mark(float(row.get('math_mark')),
                                float(row.get('physics_mark')),
                                float(row.get('chemistry_mark')))
                    student = cls(
                        int(str(i+1)),
                        row.get('name'),
                        row.get('gender'),
                        int(row.get('age')),
                        mark
                    )
                    i += 1
                    Student.ls_student.append(student)
                return Student.ls_student
        else:
            return -1

    def __repr__(self):
        return f"Student({self.student_id}, {self.name}, {self.gender}, {self.age}, {self.get_mark().get_math_mark()}, {self.get_mark().get_physics_mark()}, {self.get_mark().get_chemistry_mark()}, {self.get_average_mark()}, {self.calc_performance()})"
