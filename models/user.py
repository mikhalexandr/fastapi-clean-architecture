from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base, Aliases
from shemas.user import UserSchema


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[str | None]
    created_at: Mapped[Aliases.created_at]
    updated_at: Mapped[Aliases.updated_at]

    notes: Mapped[list["NoteModel"]] = relationship(
        back_populates="user"
    )

    def to_read_model(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            name=self.name,
            description=self.description,
            notes=[note.to_read_model() for note in self.notes]
        )
