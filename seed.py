from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models import Artist, Genre, Song, engine

Base = declarative_base()

session = sessionmaker()
session.configure(bind=engine)
Base.metadata.bind = engine

session = session()

dead = Artist(name="Grateful Dead")
stones = Artist(name="Rolling Stones")
beatles = Artist(name="Beatles")
prince = Artist(name="Prince")
mj = Artist(name="Michael Jackson")

classic_rock = Genre(name="Classic Rock")
r_and_b = Genre(name="R&B")

althea = Song(name="Althea")
scarlet_begonias = Song(name="Scarlet Begonias")
loving_cup = Song(name="Loving Cup")
stray_cat_blues = Song(name="Stray Cat Blues")
hey_jude = Song(name="Hey Jude")
nineteen_ninety_nine = Song(name="1999")
will_you_be_there = Song(name="Will You Be There")
purple_rain = Song(name="Purple Rain")

classic_rock.songs.append(althea)
classic_rock.songs.append(scarlet_begonias)
classic_rock.songs.append(hey_jude)
classic_rock.songs.append(loving_cup)
classic_rock.songs.append(stray_cat_blues)
classic_rock.songs.append(nineteen_ninety_nine)

r_and_b.songs.append(purple_rain)
r_and_b.songs.append(will_you_be_there)

dead.songs.append(althea)
dead.songs.append(scarlet_begonias)
stones.songs.append(loving_cup)
stones.songs.append(stray_cat_blues)
beatles.songs.append(hey_jude)
prince.songs.append(nineteen_ninety_nine)
prince.songs.append(purple_rain)
mj.songs.append(will_you_be_there)

session.add_all([dead, stones, beatles, prince, mj])
session.add_all([classic_rock, r_and_b])

session.commit()
