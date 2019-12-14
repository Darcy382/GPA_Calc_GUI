gpa_scale = {
    'A': 4.0,
    'A-': 3.67,
    'B+': 3.33,
    'B': 3.00,
    'B-': 2.67,
    'C+': 2.33,
    'C': 2.00,
    'D': 1.00,
    'F': 0.00
}

class Course:
    def __init__(self, course_name, grade, credits):
        self.name = course_name
        self.grade = grade
        self.credits = float(credits)

    def gpa_value(self):
        return gpa_scale[self.grade] * self.credits
