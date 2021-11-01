from typing import Optional
from pydantic import BaseModel, Field


class StreamForm(BaseModel):
    title: str
    topic: str
