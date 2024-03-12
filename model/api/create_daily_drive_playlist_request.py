from typing import Optional
from pydantic import BaseModel


class SelectedPodcast(BaseModel):
    id: str
    name: str
    backup: Optional["SelectedPodcast"] = None
    most_recent: bool


class SelectedArtist(BaseModel):
    id: str
    name: Optional[str] = None


class CreateDailyDrivePlaylistRequest(BaseModel):
    number_of_songs: int
    songs_between: int
    artists: list[SelectedArtist]
    podcasts: list[SelectedPodcast]
    day: str
    clean: bool
    debug: bool
