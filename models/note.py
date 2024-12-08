from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base, Aliases
from shemas.note import NoteSchema


class NoteModel(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), ondelete="CASCADE")
    title: Mapped[str]
    description: Mapped[str | None]
    created_at: Mapped[Aliases.created_at]
    updated_at: Mapped[Aliases.updated_at]

    user: Mapped["UserModel"] = relationship(
        back_populates="notes"
    )

    def to_read_model(self) -> NoteSchema:
        return NoteSchema(
            id=self.id,
            user_id=self.user_id,
            title=self.title,
            description=self.description,
            user=self.user.to_read_model()
        )
