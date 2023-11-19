class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lectory(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
 
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def __str__(self):
        length = 0
        score = 0
        for i in range(len(list(self.grades.values()))):
            length += len(list(self.grades.values())[i])
            score += sum(list(self.grades.values())[i])
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {round(score/length, 1)}\nКурсы в процессе изучения: {', '.join(self.courses_in_progress)}\nЗавершенные курсы: {', '.join(self.finished_courses)}"

    def __eq__(self, other): 
        length_self = 0
        score_self = 0
        for i in range(len(list(self.grades.values()))):
            length_self += len(list(self.grades.values())[i])
            score_self += sum(list(self.grades.values())[i])

        length_other = 0
        score_other = 0
        for i in range(len(list(other.grades.values()))):
            length_other += len(list(other.grades.values())[i])
            score_other += sum(list(other.grades.values())[i])
        
        return round(score_self/length_self, 1) == round(score_other/score_self, 1)
        


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor): 
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        length = 0
        score = 0
        for i in range(len(list(self.grades.values()))):
            length += len(list(self.grades.values())[i])
            score += sum(list(self.grades.values())[i])
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {round(score/length, 1)}"

    def __eq__(self, other): 
        length_self = 0
        score_self = 0
        for i in range(len(list(self.grades.values()))):
            length_self += len(list(self.grades.values())[i])
            score_self += sum(list(self.grades.values())[i])

        length_other = 0
        score_other = 0
        for i in range(len(list(other.grades.values()))):
            length_other += len(list(other.grades.values())[i])
            score_other += sum(list(other.grades.values())[i])
        
        return round(score_self/length_self, 1) == round(score_other/score_self, 1)

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
        return f"Имя: {self.name}\nФамилия: {self.surname}"

best_student = Student('Pantik', 'Shmantik', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Java']
best_student.finished_courses += ['Введение в программирование']

best_student_2 = Student('Elena', 'Ivanovna', 'your_gender')
best_student_2.courses_in_progress += ['Python']
best_student_2.courses_in_progress += ['Введение в программирование']
best_student.finished_courses += ['Java']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

cool_reviewer_2 = Reviewer('Ivan', 'Ivanov')
cool_reviewer_2.courses_attached += ['Java']
cool_reviewer_2.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student_2, 'Python', 7)

cool_reviewer_2.rate_hw(best_student_2, 'Python', 5)
cool_reviewer_2.rate_hw(best_student, 'Java', 8)

cool_lecturer = Lecturer('Nana', 'Timurovna')
cool_lecturer.courses_attached += ['Python']
cool_lecturer.courses_attached += ['Java']

cool_lecturer_2 = Lecturer('Aramchik', 'Gusanov')
cool_lecturer_2.courses_attached += ['Python']
cool_lecturer_2.courses_attached += ['Введение в программирование']

best_student.rate_lectory(cool_lecturer, 'Python', 10)
best_student_2.rate_lectory(cool_lecturer, 'Python', 8)
best_student.rate_lectory(cool_lecturer_2, 'Python', 8)
best_student_2.rate_lectory(cool_lecturer_2, 'Введение в программирование', 9)

print(cool_reviewer)
print()
print(cool_reviewer_2)
print()
print(cool_lecturer)
print()
print(cool_lecturer_2)
print()
print(best_student)
print()
print(best_student_2)
