
def menu():
    switch = {
        1: 'You choose update information of student by ID',
        2: 'You choose to delete student by ID',
        3: 'You choose to search student by Name',
        4: 'You choose to sort student order to GPA',
        5: 'You choose to sort student by Name',
        6: 'You choose to sort student by ID',
        7: 'You choose to display list student'
    }
    return switch


def main():
    print("1. Update information of student by ID")
    print("2. Delete student by ID")
    print("3. Search student by name")
    print("4. Sort student order to GPA")
    print("5. Sort student by name")
    print("6. Sort student by ID")
    print("7. Display list students")
    choose = input("Input what function you want to do?")
    print(menu())


if __name__ == "__main__":
    main()
