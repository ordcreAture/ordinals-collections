import os
import json

COLLECTIONS = "./collections"


def test_home_structure():
    expected_directories = [
        "LICENSE",
        "requirements.txt",
        ".pytest_cache",
        "tests",
        "README.md",
        "env",
        ".gitignore",
        ".git",
        "collections",
        ".circleci",
        "notebooks",
    ]
    current_directories = os.listdir()
    correct_directories = [x in expected_directories for x in current_directories]
    assert all(correct_directories), 'Top level changes are not allowed'


def test_collections_structure():
    current_collections = os.listdir(COLLECTIONS)
    folders = [
        not os.path.isfile("{}/{}".format(COLLECTIONS, x)) for x in current_collections
    ]
    assert all(folders), 'Invalid structure, include your files in a nested directory'


def test_meta():
    expected_meta = {
        "name": "Based Apes",
        "inscription_icon": "159f5b1437375424ba798c92f10670f19baf3e5d10be3bf5fbd4d4a50cf642ddi0",
        "supply": "100",
        "slug": "based-apes",
        "description": "",
        "twitter_link": "https://twitter.com/BasedApes",
        "discord_link": "https://discord.com/invite/ordinalswallet",
        "website_link": "",
    }
    current_collections = os.listdir(COLLECTIONS)

    for x in current_collections:
        with open("{}/{}/meta.json".format(COLLECTIONS, x), "r") as file:
            meta = json.load(file)

        set(meta.keys()) == set(expected_meta.keys()) , 'Invalid meta data keys'

        for y in meta.values():
          assert isinstance(y, str) , 'Invalid data type, use a string'

          assert (len(meta.get('inscription_icon')) == 66), 'Invalid inscription Id'

def test_inscriptions():
    current_collections = os.listdir(COLLECTIONS)

    for x in current_collections:
        with open("{}/{}/inscriptions.json".format(COLLECTIONS, x), "r") as file:
            insciptions = json.load(file)

        for y in insciptions:
          assert len(y.get('id')) == 66
          assert isinstance(y.get('meta').get('name'), str)