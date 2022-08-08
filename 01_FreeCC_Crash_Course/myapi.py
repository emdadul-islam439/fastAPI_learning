from fastapi import FastAPI, Path

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
def get_student(student_id: int = Path(None, description = "The ID of the student you want to view")):
    if student_id in students:
        return students[student_id]
    else:
        return {"data" : "Not found"}


# api end-point with query-parameter
@app.get("/get-by-name")
def get_student(name : str):
    for student_id in students:
        if students[student_id]['Name'] == name:
            return students[student_id]

    return {'data' : 'Not found'}


# api end-point with path-parameter and query-parameter
@app.get("/get-by-id-and-name/{student_id}")
def get_student(student_id: int, name : str):
    if student_id in students:
        if students[student_id]['Name'] == name:
            return students[student_id] 
        else:
            return {'data' : "Name doesn't match"}  
    else:
        return {'data' : 'ID not found'}

# path-query combined with OPTIONAL parameter
@app.get("/get-by-id-or-name-/{student_id}")
def get_student(student_id: int, name : str = None):
    if student_id in students:
        if (name == None) or (students[student_id]['Name'] == name):
            return students[student_id] 
        else:
            return {'data' : "Couldn't found data"}  
    else:
        return {'data' : 'ID not found'}

