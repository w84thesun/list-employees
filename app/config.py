from os import environ

from dotenv import parser

ConfigValidationError = Exception("Failed to validate config")


class Config:
    MONGO_URI: str = environ.get("MONGO_URI")
    MONGO_DB: str = environ.get("MONGO_DB")

    def valid(self) -> bool:
        if self.MONGO_DB == "":
            return False
        elif self.MONGO_URI == "":
            return False
        else:
            return True


config = Config()
