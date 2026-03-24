from sqlalchemy import Table, Column, Integer, String
from database import metadata

# Students table definition
students = Table(
    "students",
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('name', String(50), nullable=False),
    Column('age', Integer),
    Column('city', String(50))
)