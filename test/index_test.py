import unittest, sys
sys.path.insert(0, '..')
from models import *
from queries import query_experimentation

exec(open("./seed.py").read())

class TestAssociationObject(unittest.TestCase):
    def test_artists(self):
        self.assertEqual(len(session.query(Artist).all()), 5)

    def test_genres(self):
        self.assertEqual(len(session.query(Genre).all()), 2)

    def test_songs(self):
        self.assertEqual(len(session.query(Song).all()), 8)

    def test_artists_have_many_songs(self):
        dead = session.query(Artist).filter_by(name="Grateful Dead").one()
        self.assertEqual(len(dead.songs), 2)
        self.assertEqual(dead.songs[0].name, 'Althea')
        self.assertEqual(dead.songs[1].name, 'Scarlet Begonias')

    def test_artists_have_many_genres(self):
        prince = session.query(Artist).filter_by(name="Prince").one()
        self.assertEqual(len(prince.genres), 2)
        self.assertEqual(prince.genres[0].name, 'Classic Rock')
        self.assertEqual(prince.genres[1].name, 'R&B')

    def test_genres_have_many_songs(self):
        classic_rock = session.query(Genre).filter_by(name="Classic Rock").one()
        self.assertEqual(len(classic_rock.songs), 6)

    def test_genres_have_many_artists(self):
        classic_rock = session.query(Genre).filter_by(name="Classic Rock").one()
        self.assertEqual(len(classic_rock.artists), 4)

    def test_queries_experimenting(self):
        query_experimentation(session)
