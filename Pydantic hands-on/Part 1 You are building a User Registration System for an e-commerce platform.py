from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict
from pydantic import field_validator
import re

# Address Model

class Address(BaseModel):
    city: str = Field(min_lengeth=3)
    pincode: str

    # Pincode must be exactly 6 digits
    @field_validator('pincode')
    @classmethod
    def validate_pincode(cls, value: str) -> str:
        if not re.fullmatch(r'\d{6}', value):
            raise ValueError('Pincode must be exactly 6 digits')
        return value

# User Model

class User(BaseModel):
    model_config = ConfigDict(validate_asignment=True)

    user_id: int
    name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(gt=18)
    address: Address
    is_premium: Optional[bool] = False