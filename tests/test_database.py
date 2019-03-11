import os
from shutil import copyfile

from castero.episode import Episode
from castero.feed import Feed
from castero.database import Database

my_dir = os.path.dirname(os.path.realpath(__file__))


def test_database_from_json(prevent_modification):
    copyfile(my_dir + "/datafiles/feeds_working", Database.OLD_PATH)
    mydatabase = Database()

    feeds = mydatabase.feeds()
    assert len(feeds) == 2
    assert feeds[0].key == "feed key"
    assert feeds[0].title == "feed title"
    assert feeds[0].description == "feed description"
    assert feeds[0].link == "feed link"
    assert feeds[0].last_build_date == "feed last_build_date"
    assert feeds[0].copyright == "feed copyright"
    episodes0 = mydatabase.episodes(feeds[0])
    assert episodes0[0][1].title == "episode title"
    assert episodes0[0][1].description == "episode description"
    assert episodes0[0][1].link == "episode link"
    assert episodes0[0][1].pubdate == "episode pubdate"
    assert episodes0[0][1].copyright == "episode copyright"
    assert episodes0[0][1].enclosure == "episode enclosure"

    assert feeds[1].key == "http://feed2_url"
    assert feeds[1].title == "feed2 title"
    assert feeds[1].description == "feed2 description"
    assert feeds[1].link == "feed2 link"
    assert feeds[1].last_build_date == "feed2 last_build_date"
    assert feeds[1].copyright == "feed2 copyright"
    episodes1 = mydatabase.episodes(feeds[1])
    assert episodes1[0][1].title == "episode title"
    assert episodes1[0][1].description == "episode description"
    assert episodes1[0][1].link == "episode link"
    assert episodes1[0][1].pubdate == "episode pubdate"
    assert episodes1[0][1].copyright == "episode copyright"
    assert episodes1[0][1].enclosure == "episode enclosure"
