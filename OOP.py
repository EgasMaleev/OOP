class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_course.append(course_name)

    def rate_lecrute(self, lecrute, course, grade):
        if isinstance(lecrute, Lecrute):
            if course in lecrute.grades and course in self.courses_in_progress and course in lecrute.courses_attached:
                lecrute.grades[course] += [grade]
            else:
                lecrute.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        i = 0
        sum = 0
        fin_course = ''
        progress_course = ''
        for value in self.grades.values():
            for k in value:
                sum += k
                i += 1
        for value in self.finished_courses:
            fin_course += value
        for value in self.courses_in_progress:
            progress_course += value
        res = f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за домашние задания: {sum / i}\n'
        res += f' Курсы в процессе изучения: {progress_course}\n Завершенные курсы: {fin_course}'
        return res

    def __lt__(self, student2):
        i = 0
        sum = 0
        for value in self.grades.values():
            for k in value:
                sum += k
                i += 1
        middle1 = sum / i

        i = 0
        sum = 0
        for value in student2.grades.values():
            for k in value:
                sum += k
                i += 1
        middle2 = sum / i
        return (middle1 < middle2)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\n'
        res += f'Фамилия: {self.surname}'
        return res


class Lecrute(Mentor):
    def __init__(self, name, username):
        super().__init__(name, username)
        self.grades = {}
        self.courses_attached = []

    def __str__(self):
        i = 0
        sum = 0
        for value in self.grades.values():
            for k in value:
                sum += k
                i += 1
        res = f' Имя: {self.name}\n Фамилия: {self.surname}\n Средняя оценка за лекции: {sum / i}'
        return res

    def __lt__(self, lecrute2):
        i = 0
        sum = 0
        for value in self.grades.values():
            for k in value:
                sum += k
                i += 1
        middle1 = sum / i

        i = 0
        sum = 0
        for value in lecrute2.grades.values():
            for k in value:
                sum += k
                i += 1
        middle2 = sum / i
        return (middle1 < middle2)


best_lecrute = Lecrute('Petr', 'Ivanov')
best_lecrute.courses_attached += ['Python']

best_lecrute2 = Lecrute('Ivan', 'Petrov')
best_lecrute2.courses_attached += ['Python']

best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

best_student2 = Student('Tim', 'Filby', 'man')
best_student2.courses_in_progress += ['Python']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)

cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 9)
cool_mentor.rate_hw(best_student2, 'Python', 9)

best_student.rate_lecrute(best_lecrute, 'Python', 10)
best_student.rate_lecrute(best_lecrute, 'Python', 9)
best_student.rate_lecrute(best_lecrute, 'Python', 8)

best_student.rate_lecrute(best_lecrute2, 'Python', 10)
best_student.rate_lecrute(best_lecrute2, 'Python', 9)
best_student.rate_lecrute(best_lecrute2, 'Python', 10)

print(best_student.grades)
print(best_lecrute.grades)

print(cool_mentor)
print(best_lecrute)
print(best_student)
print(best_student2)
print(best_student < best_student2)
print(best_lecrute < best_lecrute2)


def middle_grade(spisok, kyrs):
    for student in spisok:
        if isinstance(student, Student):
            sum = 0
            i = 0
            for value in student.grades.values():
                for k in value:
                    sum += k
                    i += 1
                print(f'Средний балл студента {student.name} {student.surname} равен {sum / i}')

        else:
            print('Ошибка')


def middle_grade_lecrute(spisok, kyrs):
    for lecrute in spisok:
        if isinstance(lecrute, Lecrute):
            sum = 0
            i = 0
            for value in lecrute.grades.values():
                for k in value:
                    sum += k
                    i += 1
                print(f'Средний балл лектора {lecrute.name} {lecrute.surname} равен {sum / i}')
        else:
            print('Ошибка')
            
middle_grade([best_student, best_student2], 'Python')
middle_grade_lecrute([best_lecrute, best_lecrute2], 'Python')