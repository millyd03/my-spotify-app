from typing import Optional
from pydantic import BaseModel


class SelectedArtist(BaseModel):
    id: str
    name: Optional[str] = None


class OtherUser(BaseModel):
    client_id: str
    client_secret: str
    artists: list[SelectedArtist]
    name: Optional[str] = None


class CreateBlendedPlaylistRequest(BaseModel):
    number_of_songs: int
    artists: list[SelectedArtist]
    other_users: list[OtherUser]
    clean: bool
    debug: bool
