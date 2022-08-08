from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1: {
        "Name" : "Student 1",
        "age" : "20",
        "year" : "year 11",
    },
    2: {
        "Name" : "Student 2",
        "age" : "22",
        "year" : "year 13",
    }
}


class Student(BaseModel):
    Name : str
    age : int
    year : str


class UpdateStudent(BaseModel):
    Name : Optional[str] = None
    age : Optional[int] = None
    year : Optional[str] = None


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


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return { "Error" : "Student ID already exists" }
    
    students[student_id] = student
    return students[student_id]



@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return { "Error" : "Student ID not found" }

    if student.Name != None:
        students[student_id]['Name'] = student.Name

    if student.age != None:
        students[student_id]['age'] = student.age
    
    if student.year != None:
        students[student_id]['year'] = student.year

    return students[student_id]



@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return { "Error" : "Student ID not found" }
    
    del students[student_id]
    return { "Message" : "Successfully deleted student" }