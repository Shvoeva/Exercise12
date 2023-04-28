default_surname = 'Петров'
default_name = 'Петр'
default_patronymic = 'Петрович'
default_year = 2000
default_course = 1
default_group = '100'
default_grades = {'': 2, '': 2, '': 2, '': 2, '': 2}

max_grade = 5
min_grade = 2
count_grade = 5

first_course = 1
sixth_course = 6

min_year = 1900
max_year = 2023

class Student:
    def __init__(self, surname=default_surname, name=default_name, patronymic=default_patronymic, year=default_year,
                 grades=default_grades):

        self.Surname = surname if surname.isalpha() else default_surname
        self.Name = name if name.isalpha() else default_name
        self.Patronymic = patronymic if patronymic.isalpha() else default_patronymic

        self.Surname = self.Surname.title() if not surname.istitle() else self.Surname
        self.Name = self.Name.title() if not name.istitle() else self.Name
        self.Patronymic = self.Patronymic.title() if not patronymic.istitle() else self.Patronymic

        self.Year = default_year if year < min_year or year > max_year or type(year) is not int else year

        if (len(grades) != count_grade):
            self.Grades = default_grades
        else:
            for subject, grade in grades.items():
                if grade < min_grade or grade > max_grade or type(grade) is not int or type(subject) is not str:
                    self.Grades = default_grades
                    return

            self.Grades = grades

    def get_gpa(self):
        gpa = 0
        for grade in self.Grades.values():
            gpa += grade

        return gpa / len(self.Grades)

class Group:
    def __init__(self, course=default_course, group=default_group, *students: Student):
        self.Students = list(students[0] if len(students) == 1 else students)
        self.Group = group
        self.Course = default_course if course < first_course or course > sixth_course or type(course) is not int else course

    def get_gpa(self):
        gpa = 0
        for student in self.Students:
            gpa += student.get_gpa()

        return gpa / len(self.Students)

    def get_subject_average(self, subject: str):
        average = 0
        for student in self.Students:
            average += student.Grades[subject]

        return average / len(self.Students)

if __name__ == '__main__':
    student1 = Student('Петров', 'Антон', 'Петрович', 2000, {'information security': 5,
                                                             'parallel programming': 4,
                                                             'distributed computing systems': 5,
                                                             'theory of programming languages': 5,
                                                             'undergraduate practice': 5
                                                             }
                       )
    student2 = Student('Тихонов', 'Константин', 'Владимирович', 1999, {'information security': 4,
                                                                       'parallel programming': 4,
                                                                       'distributed computing systems': 4,
                                                                       'theory of programming languages': 4,
                                                                       'undergraduate practice': 4
                                                                       }
                       )
    student3 = Student('Пятифанов', 'Роман', 'Петрович', 2000, {'information security': 5,
                                                                'parallel programming': 4,
                                                                'distributed computing systems': 4,
                                                                'theory of programming languages': 4,
                                                                'undergraduate practice': 5
                                                                }
                       )
    group108 = Group(4, '108', student1, student2, student3)

    print(f"\tСредний балл студента1: {student1.get_gpa()}")
    print(f"\tСредний балл студента2: {student2.get_gpa()}")
    print(f"\tСредний балл студента3: {student3.get_gpa()}")
    print(f"\tСредний балл группы 108: {group108.get_gpa()}")
    print(f"\tСредний балл по information security в группе 108: {group108.get_subject_average('information security')}")

    group100 = Group(2, '100',
        Student('Матюхин', 'Владимир', 'Сергеевич', 2002, {'mathematics': 4,
                                                           'foreign language': 4,
                                                           'probability theory': 3,
                                                           'object-oriented programming': 4,
                                                           'physical training': 5
                                                           }
                ),
        Student('Бабурин', 'Семен', 'Семенович', 2002, {'mathematics': 2,
                                                        'foreign language': 4,
                                                        'probability theory': 4,
                                                        'object-oriented programming': 3,
                                                        'physical training': 4
                                                        }
                ),
        Student('Дронин', 'Михаил', 'Михайлович', 2002, {'mathematics': 4,
                                                         'foreign language': 3,
                                                         'probability theory': 5,
                                                         'object-oriented programming': 4,
                                                         'physical training': 4
                                                         }
                )
                     )

    group109 = Group(3, '109',
        Student('Смирнова', 'Екатерина', 'Семеновна', 2001, {'physical training': 5,
                                                             'life safety': 5,
                                                             'OS': 5,
                                                             'networks and telecommunications': 3,
                                                             'optimization methods': 5
                                                             }
                ),
        Student('Талалаева', 'Ксения', 'Анатольевна', 2002, {'physical training': 5,
                                                             'life safety': 4,
                                                             'OS': 3,
                                                             'networks and telecommunications': 4,
                                                             'optimization methods': 4
                                                             }
                ),
        Student('Морозова', 'Полина', 'Марковна', 2001, {'physical training': 5,
                                                         'life safety': 5,
                                                         'OS': 5,
                                                         'networks and telecommunications': 5,
                                                         'optimization methods': 5
                                                         }
                )
                     )