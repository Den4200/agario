from datetime import datetime

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    DateTime
)
from sqlalchemy.orm import relationship

from frost.server.database import Base


class Match(Base):
    __tablename__ = 'matches'

    id = Column(Integer, primary_key=True, nullable=False)

    place = Column(Integer, nullable=False)
    score = Column(Integer, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship('User')

    def __repr__(self) -> str:
        return (
            f'<{type(self).__name__} id={self.id!r} user_id={self.user_id!r} '
            f'score={self.score!r} place={self.place!r}>'
        )
