from pydantic import BaseModel


class NoteSchema(BaseModel):
    id: int
    user_id: str
    title: str
    description: str | None
    user: dict

    class Config:
        from_attributes = True
