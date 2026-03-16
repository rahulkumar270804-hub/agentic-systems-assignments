from fastapi import FastAPI, Depends
from sqlalchemy import insert, select, update, delete
from database import get_db, metadata, engine
from models import students

app = FastAPI()

# Create table
metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management System API!"}

# Insert students
@app.post("/insert")
def insert_students(db=Depends(get_db)):

    stmt = insert(students).values([
        {"name": "Rahul", "age": 20, "city": "Ahmedabad"},
        {"name": "Abhishek", "age": 22, "city": "Deheradun"},
        {"name": "Prakhar", "age": 21, "city": "Varanasi"}
    ])

    db.execute(stmt)
    db.commit()

    return {"message": "Students inserted successfully"}

# Fetch all students
@app.get("/students")
def get_students(db=Depends(get_db)):
    stmt = select(students)
    result = db.execute(stmt)
    return {"students": [dict(row) for row in result]}

# Update student information
@app.put("/update")
def update_city(db = Depends(get_db)):

    stmt = update(students).where(
        students.c.name == "Rahul"
    ).values(city="Ahmedabad")

    db.execute(stmt)
    db.commit()
    return {"message": "Student city updated successfully"}

# Delete a student age < 20
@app.delete("/delete")
def delete_students(db = Depends(get_db)):

    stmt = delete(students).where(students.c.age < 20)
    db.execute(stmt)
    db.commit()
    return {"message": "Students with age < 20 deleted successfully"}

