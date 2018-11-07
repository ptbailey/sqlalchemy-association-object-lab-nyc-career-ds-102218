from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

# Write your classes below

class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    songs = relationship('Song', back_populates = 'artist') #parameter that
    #establishes the relationship to the Song model and back_populates to the
    #artist property of the Song model
    genres = relationship('Genre', secondary='song', back_populates='artists')
    #relationship('Name of reference class', secondary = 'tablename of association
    #table', back_populates = reference class attribute with relationship to this class)

class Genre(Base):
    __tablename__ = 'genre'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    songs = relationship('Song', back_populates = 'genre')#parameter that
    #establishes the relationship to the Song model and back_populates to the
    #genre attribute of the Song model
    artists = relationship('Artist', secondary='song', back_populates='genres')
    #relationship('Name of reference class', secondary = 'tablename of association
    #table', back_populates =reference class attribute with relationship to this class)

class Song(Base):
    __tablename__ = 'song'
    id = Column(Integer, primary_key = True)
    name = Column(String)
    artist_id = Column(Integer, ForeignKey('artist.id'))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    artist = relationship(Artist, back_populates = 'songs')
    genre = relationship(Genre, back_populates = 'songs')


engine = create_engine('sqlite:///:memory:')
Base.metadata.create_all(engine)
