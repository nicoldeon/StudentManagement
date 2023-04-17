from Mark import Mark
from Student import Student
import csv
import os.path
import sys


class StudentManagement:
    def __init__(self, ls_students=None):
        self.ls_students = ls_students

    def sort_student_by_gpa(self):
        """ Method to sort student asc by student's gpa"""
        return sorted(self.ls_students,
                      key=lambda x: x.get_average_mark())

    def sort_student_by_name(self):
        """ Method to sort student asc by student's name"""
        return sorted(self.ls_students, key=lambda x: x.get_name())

    def sort_student_by_id(self):
        """ Method to sort student asc by student's id"""
        return sorted(self.ls_students,
                      key=lambda x:  int(x.get_student_id()))

    def find_student_by_name(self, name):
        """ Method to find student by student's name"""
        for student in self.ls_students:
            if student.get_name() == name:
                return student
        return -1

    def get_student_by_id(self, id_student):
        for student in self.ls_students:
            if student.get_student_id() == id_student:
                return student
        return -1

    def update_student_by_id(self, id_student):
        """ Method to update student by student'id """
        student = self.get_student_by_id(id_student)
        if student is not None:
            student.set_name()
            student.set_gender()
            student.set_age()
            student.set_mark()
            self.save_data()

    def delete_student_by_id(self, id_student):
        """ Method to delete student by student's id """
        student = self.get_student_by_id(id_student)
        if student is not None:
            self.ls_students.remove(student)
            self.save_data()

    def save_data(self, url_path='Student.csv', *agrs, **kwargs):
        with open(url_path, "w") as f:
            writer = csv.writer(f)
            writer.writerow(['student_id', 'name', 'gender', 'age', 'math_mark',
                             'physics_mark', 'chemistry_mark'])
            for student in self.ls_students:
                writer.writerow([
                    '',
                    student.get_name(),
                    student.get_gender(),
                    student.get_age(),
                    student.get_mark().get_math_mark(),
                    student.get_mark().get_physics_mark(),
                    student.get_mark().get_chemistry_mark()
                ])

    def display_list_student(self):
        print('{:<15s} {:<20s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<10s}'.format(
            "Student ID", "Name", "Gender", "Age", "Math Mark", "Physics Mark", "Chemistry Mark", "Average Mark", "Performance"))
        print('-'*140)
        for student in self.ls_students:
            print('{:<15} {:<20} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15.2f} {:<10}'.format(
                student.get_student_id(), student.get_name(
                ), student.get_gender(), student.get_age(),
                student.get_mark().get_math_mark(), student.get_mark().get_physics_mark(),
                student.get_mark().get_chemistry_mark(), student.get_average_mark(), student.calc_performance()))

    def display_student(self, ls_students):
        print('{:<15s} {:<20s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<10s}'.format(
            "Student ID", "Name", "Gender", "Age", "Math Mark", "Physics Mark", "Chemistry Mark", "Average Mark", "Performance"))
        print('-'*140)
        for student in ls_students:
            print('{:<15} {:<20} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15.2f} {:<10}'.format(
                student.get_student_id(), student.get_name(
                ), student.get_gender(), student.get_age(),
                student.get_mark().get_math_mark(), student.get_mark().get_physics_mark(),
                student.get_mark().get_chemistry_mark(), student.get_average_mark(), student.calc_performance()))

    def display(self, student):
        print('{:<15s} {:<20s} {:<10s} {:<10s} {:<15s} {:<15s} {:<15s} {:<15s} {:<10s}'.format(
            "Student ID", "Name", "Gender", "Age", "Math Mark", "Physics Mark", "Chemistry Mark", "Average Mark", "Performance"))
        print('-'*140)
        print('{:<15} {:<20} {:<10} {:<10} {:<15} {:<15} {:<15} {:<15.2f} {:<10}'.format(
            student.get_student_id(), student.get_name(
            ), student.get_gender(), student.get_age(),
            student.get_mark().get_math_mark(), student.get_mark().get_physics_mark(),
            student.get_mark().get_chemistry_mark(), student.get_average_mark(), student.calc_performance()))
