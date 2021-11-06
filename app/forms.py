from typing import Optional
from pydantic import BaseModel


class StreamForm(BaseModel):
    title: str
    topic: str
    status: Optional[str] = None
    description: Optional[str] = None


class StreamUpdateForm(BaseModel):
    stream_id: int
    status: str


class UserCreateForm(BaseModel):
    email: str
    password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    nickname: Optional[str] = None


class UserLoginForm(BaseModel):
    email: str
    password: str
