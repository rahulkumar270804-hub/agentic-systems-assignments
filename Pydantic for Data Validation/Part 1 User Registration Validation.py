from pydantic import BaseModel, Field, EmailStr
from pydantic import ValidationError

class UserRegister(BaseModel):
    username: str = Field(min_length=5, max_length=50)
    email: EmailStr
    age: int = Field(ge=18)

#valid example
valid_data = {
    "username": "Rahul Kumar",
    "email": "rahul.kumar@example.com",
    "age": 25
}

user = UserRegister(**valid_data)
print(user)

#invalid example
invalid_data = {
    "username": "rah",
    "email": "invalid_email",
    "age": 17
}

try:
    UserRegister.model_validate(invalid_data)
except ValidationError as e:
    print(e)