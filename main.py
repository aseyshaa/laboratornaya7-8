class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_info(self):
        print(f"Имя: {self.name}, Возраст: {self.age}, Пол: {self.gender}")


class Student(Person):
    def __init__(self, name, age, gender, student_id, major):
        super().__init__(name, age, gender)
        self.student_id = student_id
        self.major = major

    def get_info(self):
        super().get_info()
        print(f"Студенческий ID: {self.student_id}, Специальность: {self.major}")


class Teacher(Person):
    def __init__(self, name, age, gender, teacher_id, department):
        super().__init__(name, age, gender)
        self.teacher_id = teacher_id
        self.department = department

    def get_info(self):
        super().get_info()
        print(f"ID преподавателя: {self.teacher_id}, Кафедра: {self.department}")


class DepartmentHead(Teacher):
    def __init__(self, name, age, gender, teacher_id, department, department_name):
        super().__init__(name, age, gender, teacher_id, department)
        self.department_name = department_name

    def get_info(self):
        super().get_info()
        print(f"Название кафедры: {self.department_name}")


def add_person(person_list):
    name = input("Введите имя: ")
    age = input("Введите возраст: ")
    gender = input("Введите пол: ")
    choice = input("Выберите роль (1 - Студент, 2 - Преподаватель, 3 - Заведующий кафедрой): ")

    if choice == "1":
        student_id = input("Введите студенческий ID: ")
        major = input("Введите специальность: ")
        person = Student(name, age, gender, student_id, major)
    elif choice == "2":
        teacher_id = input("Введите ID преподавателя: ")
        department = input("Введите кафедру: ")
        person = Teacher(name, age, gender, teacher_id, department)
    elif choice == "3":
        teacher_id = input("Введите ID преподавателя: ")
        department = input("Введите кафедру: ")
        department_name = input("Введите название кафедры: ")
        person = DepartmentHead(name, age, gender, teacher_id, department, department_name)
    else:
        print("Некорректный выбор!")
        return

    person_list.append(person)
    print("Человек успешно добавлен!")


def view_students(person_list):
    print("Студенты:")
    for person in person_list:
        if isinstance(person, Student):
            person.get_info()
            print()


def view_teachers(person_list):
    print("Преподаватели:")
    for person in person_list:
        if isinstance(person, Teacher):
            person.get_info()
            print()


def view_department_heads(person_list):
    print("Заведующие кафедрой:")
    for person in person_list:
        if isinstance(person, DepartmentHead):
            person.get_info()
            print()


def main():
    person_list = []

    while True:
        print("1. Добавить человека")
        print("2. Посмотреть список студентов")
        print("3. Посмотреть список преподавателей")
        print("4. Посмотреть список заведующих кафедрой")
        print("5. Выйти")
        choice = input("Введите ваш выбор: ")

        if choice == "1":
            add_person(person_list)
        elif choice == "2":
            view_students(person_list)
        elif choice == "3":
            view_teachers(person_list)
        elif choice == "4":
            view_department_heads(person_list)
        elif choice == "5":
            break
        else:
            print("Некорректный выбор!")


if __name__ == "__main__":
    main()