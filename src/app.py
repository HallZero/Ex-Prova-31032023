from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.game import Game

engine = create_engine('sqlite+pysqlite:///database.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

query = session.query(Game).all()

for game in query:
    print(f'-{game.game_name} - {game.platform} - {game.price} - {game.score}')