from pymongo import MongoClient

from app.config import config, ConfigValidationError


def connect():
    if not config.valid():
        raise ConfigValidationError

    client = MongoClient(host=config.MONGO_URI)

    db = client[config.MONGO_DB]

    try:
        db.command("ping")
    except Exception as e:
        print(e)

    collection = db.get_collection("employees")

    return collection


Conn = connect()
