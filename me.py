# name = "joshua"
# age = 12
# print(name)
# print("my first python program!")
# print (age)
#
# name = input("what is your name? ")
# age = input("what is your age? ")
# name = input("what is your surname? ")


# import fastapi
#
#
#
# app = fastapi.FastAPI()
#
# @app.get("/")
# def home():
#     return {"message": "Hello World"}




import fastapi
from fastapi.responses import FileResponse
import random

app = fastapi.FastAPI()


students = [
    {
        "name": "Victory",
        "age": 25,
        "course": "Python"
    },
    {
        "name": "John",
        "age": 22,
        "course": "JavaScript"
    },
    {
        "name": "Sarah",
        "age": 24,
        "course": "FastAPI"
    }
]


@app.get("/")
def home():
    return FileResponse("index.html")


# Show all students
@app.get("/students")
def get_students():
    return {
        "students": students
    }


# Show one student
@app.get("/student/{student_id}")
def get_student(student_id: int):

    if student_id < 0 or student_id >= len(students):
        return {
            "error": "Student not found"
        }

    return students[student_id]


# 🎲 Student of the Day
@app.get("/student-of-day")
def student_of_day():

    student = random.choice(students)

    return {
        "message": "🎉 Student of the Day!",
        "student": student["name"],
        "course": student["course"]
    }


# 📊 Course summary
@app.get("/course-summary")
def course_summary():

    courses = {}

    for student in students:

        course = student["course"]

        if course not in courses:
            courses[course] = 0

        courses[course] += 1

    return {
        "courses": courses
    }


# 💬 Motivation
@app.get("/motivation")
def motivation():

    messages = [
        "Keep learning! 🚀",
        "You are doing great! 💪",
        "Every expert was once a beginner! 🎓",
        "Keep coding! 🐍",
        "Your next project could be amazing! ⭐"
    ]

    return {
        "message": random.choice(messages)
    }