from StudentManagement import StudentManagement
from Student import Student
import sys
import os


def main():
    n = len(sys.argv)
    if n > 1:
        ls_students = Student.read_from_file(sys.argv[1], mode='r')
    else:
        ls_students = Student.read_from_file(mode='r')
    st = StudentManagement(ls_students)
    while True:
        print("1. Update information of student by ID")
        print("2. Delete student by ID")
        print("3. Search student by name")
        print("4. Sort student order to GPA")
        print("5. Sort student by name")
        print("6. Sort student by ID")
        print("7. Display list students")
        print("8. Exit")
        choice = input("Input your choice: ")
        if choice == '1':
            st.display_list_student()
            id_update = int(input("Input id student need to change: "))
            st.update_student_by_id(id_update)
            print("List student after updated")
            st.display_list_student()
        elif choice == '2':
            st.display_list_student()
            id_delete = int(input("Input id student need to delete: "))
            st.delete_student_by_id(id_delete)
            print("List student after deleted")
            st.display_list_student()
        elif choice == '3':
            st.display_list_student()
            name = input("Input name of student you want to find:")
            student = st.find_student_by_name(name)
            st.display(student)
        elif choice == '4':
            sorted_by_gpa = st.sort_student_by_gpa()
            st.display_student(sorted_by_gpa)
        elif choice == '5':
            sorted_by_name = st.sort_student_by_name()
            st.display_student(sorted_by_name)
        elif choice == '6':
            sorted_by_id = st.sort_student_by_id()
            st.display_student(sorted_by_id)
        elif choice == '7':
            st.display_list_student()
        elif choice == '8':
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
