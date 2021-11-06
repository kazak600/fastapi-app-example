from typing import Optional
from pydantic import BaseModel, Field


class StreamForm(BaseModel):
    title: str
    topic: str


class UserCreateForm(BaseModel):
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nickname: Optional[str] = None


class UserLoginForm(BaseModel):
    email: str
    password: str


class UserGetForm(BaseModel):
    email: str
    auth_token: str
