import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gradebook.models import Student, Course, Enrollment
from gradebook.storage import save_data


def seed_data():
    

    
    students = [
        Student(1, "John"),
        Student(2, "Sarah"),
        Student(3, "Alex")
    ]

    
    courses = [
        Course("CS101", "Introduction to CS"),
        Course("MA101", "Mathematics")
    ]

    
    enrollments = [
        Enrollment(1, "CS101", [90, 85]),
        Enrollment(1, "MA101", [88, 92]),
        Enrollment(2, "CS101", [78, 92]),
        Enrollment(3, "MA101", [95, 89])
    ]

    
    data = {
        "students": [
            {
                "id": student.id,
                "name": student.name
            }
            for student in students
        ],

        "courses": [
            {
                "code": course.code,
                "title": course.title
            }
            for course in courses
        ],

        "enrollments": [
            {
                "student_id": enrollment.student_id,
                "course_code": enrollment.course_code,
                "grades": enrollment.grades
            }
            for enrollment in enrollments
        ]
    }

    
    save_data(data)

    print("Sample data created successfully!")
    print("3 students added")
    print("2 courses added")
    print("4 enrollments created")
    print("Sample grades added")
    print("Data saved to data/gradebook.json")


if __name__ == "__main__":
    seed_data()
