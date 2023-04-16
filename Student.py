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
                 capacity=None):
        super().__init__(name, gender, age)
        self.student_id = student_id
        self.mark = mark
        self.average_mark = average_mark
        self.capacity = capacity

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

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, val):
        self.capacity = val

    def get_average_mark(self):
        ave_mark = self.get_mark().calc_ave_mark()
        self.set_average_mark(ave_mark)
        return self.average_mark

    def calc_capacity(self):
        average_mark = self.get_average_mark()
        math_mark = self.get_mark().get_math_mark()
        physics_mark = self.get_mark().get_physics_mark()
        chemistry_mark = self.get_mark().get_chemistry_mark()
        if average_mark >= 8 and math_mark > 8 and physics_mark > 8 and chemistry_mark > 8:
            self.set_capacity("Good")
        elif 6.5 <= average_mark < 8 and math_mark > 8 and physics_mark > 5 and chemistry_mark > 5:
            self.set_capacity("Quite good")
        elif 5 <= average_mark < 6.5 and math_mark > 5 and physics_mark > 4 and chemistry_mark > 4:
            self.set_capacity("Medium")
        elif average_mark < 5:
            self.set_capacity("Bad")
        else:
            self.set_capacity("Don't have enough value")

        return self.get_capacity()

    def sort_student_by_gpa(self):
        ls_sort = sorted(Student.ls_student, key=lambda x: x.calc_ave_mark())
        self.display_student(ls_sort)

    def sort_student_by_name(self):
        ls_sort = sorted(Student.ls_student, key=lambda x: x.get_name())
        self.display_student(ls_sort)

    def sort_student_by_id(self):
        ls_sort = sorted(Student.ls_student,
                         key=lambda x:  int(x.get_student_id()))
        self.display_student(ls_sort)

    def find_student_by_name(self):
        name_student = input("Input name of student you want to find:")
        ls_search = list(filter(lambda x: x.get_name()
                         == name_student, Student.ls_student))
        self.display_student(ls_search)

    def update_student_by_id(self):
        id_student = int(input("Input id of student you want to update"))
        stds = []
        ls_students = Student.ls_student
        is_found = False
        for row in ls_students:
            if row.get_student_id() == id_student:
                is_found = True
                data = {
                    "name": input("Input new name: "),
                    "gender": input("Input new gender: "),
                    "age": int(input("Input new age: ")),
                    "math_mark": float(input("Input math mark: ")),
                    "physics_mark": float(input("Input physics mark: ")),
                    "chemistry_mark": float(input("Input chemistry mark: "))
                }
                stds.append(data)
            else:
                stds.append(
                    {
                        "name": row.get_name(),
                        "gender": row.get_gender(),
                        "age": row.get_age(),
                        "math_mark": row.get_mark().get_math_mark(),
                        "physics_mark": row.get_mark().get_physics_mark(),
                        "chemistry_mark": row.get_mark().get_chemistry_mark()
                    }
                )
        if is_found == False:
            return -1
        with open("Student.csv", "w", newline='') as f:
            headers = ['student_id', 'name',
                       'gender', 'age', 'math_mark', 'physics_mark', 'chemistry_mark', 'average_mark', 'capacity']
            data = csv.DictWriter(f, delimiter=',', fieldnames=headers)
            data.writerow(dict((heads, heads) for heads in headers))
            data.writerows(stds)
        return Student.read_from_file()

    def delete_student_by_id(self):
        id_student = int(input("Input id of student you want to update"))
        ls_students = Student.ls_student
        stds = []
        is_found = False
        for row in ls_students:
            if int(row.get_student_id() == id_student):
                is_found = True
            else:
                stds.append(
                    {
                        "name": row.get_name(),
                        "gender": row.get_gender(),
                        "age": row.get_age(),
                        "math_mark": row.get_mark().get_math_mark(),
                        "physics_mark": row.get_mark().get_physics_mark(),
                        "chemistry_mark": row.get_mark().get_chemistry_mark()
                    }
                )
        if is_found == False:
            return -1
        return Student.read_from_file()

    def input_student(self):
        n = len(Student.ls_student)
        self.set_student_id(n)
        self.set_name()
        self.set_gender()
        self.set_age()
        self.set_mark()
        Student.ls_student.append(self)

    def display_student(self, ls_students):
        print('{:<15s} {:<20s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<10s}'.format(
            "Student ID", "Name", "Gender", "Age", "Math Mark", "Physics Mark", "Chemistry Mark", "Average Mark", "Capacity"))
        print('-'*140)
        for student in ls_students:
            print('{:<15} {:<20} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15.2f} {:<10}'.format(
                student.get_student_id(), student.get_name(
                ), student.get_gender(), student.get_age(),
                student.get_mark().get_math_mark(), student.get_mark().get_physics_mark(),
                student.get_mark().get_chemistry_mark(), student.get_average_mark(), student.calc_capacity()))

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
        return -1

    def __repr__(self):
        return f"{self.student_id}, {self.name}, {self.gender}, {self.age}, {self.get_mark().get_math_mark()}, {self.get_mark().get_physics_mark()}, {self.get_mark().get_chemistry_mark()}, {self.get_average_mark()}, {self.calc_capacity()}"


def main():
    n = len(sys.argv)
    if n > 1:
        ls_students = Student.read_from_file(sys.argv[1], mode='r')
    else:
        ls_students = Student.read_from_file(mode='r')
    st = Student()
    st.display_student(ls_students)
    print("Sort student by gpa")
    st.sort_student_by_gpa()
    print("Sort student by ID")
    st.sort_student_by_id()
    print("Sort student by name")
    st.sort_student_by_name()
    print("Find student by id:")
    st.find_student_by_name()
    ls = st.update_student_by_id()
    st.display_student(ls)
    ls_del = st.delete_student_by_id()
    st.display_student(ls_del)


if __name__ == "__main__":
    main()
