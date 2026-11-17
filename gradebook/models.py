class Student:
    def __init__(self,id,name):
        if not isinstance(name,str) or not name.strip():
            raise ValueError("Name must be a non-empty string")

        if isinstance(id, bool) or not isinstance(id, int) or id<=0:
            raise ValueError("Student ID must be a positive integer")
        
        self.id = id
        self.name = name.strip()

    def __str__(self):
        return f"Student {self.id}: {self.name}"

class Course:
    def __init__(self, code, title):
        if not isinstance(code, str) or not code.strip():
            raise ValueError("Course code cannot be empty")

        if not isinstance(title, str) or not title.strip():
            raise ValueError("Course title cannot be empty")

        self.code = code
        self.title = title

    def __str__(self):
        return f"Course Code: {self.code}, Title: {self.title}"

class Enrollment:
    def __init__(self, student_id, course_code, grades = None):
        self.student_id = student_id
        self.course_code = course_code
        self.grades = grades if grades is not None else []

        if not isinstance(self.grades, list):
            raise ValueError("Grades must be provided as a list")

        for grade in self.grades:
            if(
                isinstance(grade, bool) or not isinstance(grade, (int, float))
                or not 0 <= grade <= 100
            ):
                raise ValueError("Grades must be numeric and between 0 and 100")

        

    def __str__(self):
        return (
            f"Student ID: {self.student_id}, "
            f"Course: {self.course_code},"
            f"Grades: {self.grades}")


