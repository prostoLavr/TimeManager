from pydantic import BaseModel


class NoteSummary(BaseModel):
    minutes: int


    class Config:
        from_attributes = True


class NoteBase(BaseModel):
    minutes: int | None = None
    text: str | None = None


class NoteCreate(NoteBase):
    pass


class Note(NoteBase):
    class Config:
        from_attributes = True


class NoteUpdate(BaseModel):
    minutes: int | None
    text: str | None