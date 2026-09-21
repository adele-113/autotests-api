from pydantic import BaseModel, Field, EmailStr, HttpUrl, ValidationError, constr, ConfigDict
from pydantic.alias_generators import to_camel

class UserSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    """
    Описание структуры пользователя.
    """
    id: str
    email: EmailStr
    last_name: str
    first_name: str
    middle_name: str

class CreateUserRequestSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_by_name=True)
    """
    Описание структуры запроса на создание пользователя.
    """
    email: EmailStr
    password: str = constr(min_length=8)
    last_name: str
    first_name: str
    middle_name: str

class CreateUserResponseSchema(BaseModel):
    """
    Описание структуры ответа создания пользователя.
    """
    user: UserSchema
