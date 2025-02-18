from pydantic import BaseModel, Field, EmailStr


class CreateUser(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)



