from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models.game import Game

engine = create_engine('sqlite+pysqlite:///database.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

name = input('Game name: ')
platform = input('Platform: ')
price = input('Price: ')
score = input('Score: ')

game = Game(game_name=name, platform=platform, price=price, score=score)

session.add(game)
session.commit()

print('Game added successfully!')
