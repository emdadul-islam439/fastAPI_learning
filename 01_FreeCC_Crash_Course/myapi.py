from fastapi import FastAPI

app = FastAPI()

students = {
    1: {
        "Name" : "Student 1",
        "age" : "20",
        "class" : "year 11",
    },
    2: {
        "Name" : "Student 2",
        "age" : "22",
        "class" : "year 13",
    }
}

# api end-point without any parameter
@app.get("/")
def index():
    return {
        "name" : "First Data"
    }

# api end-point with path-parameter
@app.get("/get-student/{student_id}")
def get_student(student_id: int):
    if student_id in students:
        return students[student_id]
    else:
        return {"data" : "Not found"}