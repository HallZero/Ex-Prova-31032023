from models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True)
    game_name = Column(String(50), nullable=False)
    platform = Column(String(50), nullable=False)
    price = Column(String(50), nullable=False)
    score = Column(Integer)

    def __repr__(self) -> str:
        return f'Game {self.game_name}'