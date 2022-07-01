class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if Class.__students_count > len(self.students):
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if self.students:
            average = sum(self.grades) / len(self.grades)
            return round(average, 2)

    def __repr__(self):
        if self.students:
            return f"The students in {self.name}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}"





