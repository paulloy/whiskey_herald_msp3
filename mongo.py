import os


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "whiskey_herald"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Error. Not connected: %s") % e
