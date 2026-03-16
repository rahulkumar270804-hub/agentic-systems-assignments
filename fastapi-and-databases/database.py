from sqlalchemy import create_engine, MetaData

# Database connection setup
DATABASE_URL = "mysql://username:password@localhost/student_db"

engine = create_engine(DATABASE_URL)

# Metadata container
metadata = MetaData()

# Dependency to get DB connection
def get_db():
    with engine.connect() as conn:
        yield conn