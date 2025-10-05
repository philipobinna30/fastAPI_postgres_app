from sqlalchemy.orm import Session
import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(name=student.name, age=student.age)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(models.Student).all()

