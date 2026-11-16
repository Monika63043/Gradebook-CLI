# Gradebook CLI

A simple Python command-line application to manage students, courses, enrollments and grades.

## Features
- Add students and courses.
- Enroll students in courses.
- Add and view grades.
- Calculate course averages and GPA.
- Store data in JSON files.

## Project Structure

```text
gradebook/
├── main.py
├── gradebook/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   └── service.py
├── data/
│   └── gradebook.json
├── logs/
│   └── app.log
├── tests/
│   └── test_service.py
├── scripts/
│   └── seed.py
└── README.md
```

## Setup

Clone the repository:

```bash
git clone <your-repository-url>
cd gradebook
```

Create and activate a virtual environment:

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

No external packages are required.

## Run Sample Data

```bash
python scripts/seed.py
```

This creates 3 students, 2 courses, enrollments and sample grades in `data/gradebook.json`.

## Usage

Run commands from the project folder.

| Operation | Command |
|---|---|
| Add student | `python main.py add-student --name "John"` |
| Add course | `python main.py add-course --code CS101 --title "Intro to CS"` |
| Enroll | `python main.py enroll --student-id 1 --course CS101` |
| Add grade | `python main.py add-grade --student-id 1 --course CS101 --grade 95` |
| List students | `python main.py list students` |
| List courses | `python main.py list courses` |
| List enrollments | `python main.py list enrollments` |
| Calculate average | `python main.py avg --student-id 1 --course CS101` |
| Calculate GPA | `python main.py gpa --student-id 1` |

### Example Output

```text
Student added successfully. ID: 4

Average for student 1 in CS101: 87.50

GPA for student 1: 88.75
```

## Run Tests

```bash
python -m unittest discover -s tests -v
```

Tests cover student creation, grade addition, average calculation and an error case.

## Design decisions & limitations

- Uses JSON files for data storage.
- Uses separate modules for models, storage and business logic.
- Uses a simple mean of course averages for GPA.
- Supports numeric grades between 0 and 100.
- Provides a command-line interface only.


