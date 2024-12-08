from pydantic import BaseModel


class UserSchema(BaseModel):
    id: int
    name: str
    description: str | None
    notes: list[dict]

    class Config:
        from_attributes = True
