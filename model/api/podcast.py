from pydantic import BaseModel


class Podcast(BaseModel):
    id: str
    value: str
