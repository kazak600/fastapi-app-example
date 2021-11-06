from typing import Optional
from pydantic import BaseModel, Field


class StreamForm(BaseModel):
    title: str
    topic: str


class UserCreateForm(BaseModel):
    email: str
    password: str


class UserLoginForm(BaseModel):
    email: str
    password: str
