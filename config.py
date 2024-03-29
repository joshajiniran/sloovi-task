import datetime
import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = False
    TESTING = False
    PRODUCTION = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_EXPIRES_ON = datetime.timedelta(days=1)
    BCRYPT_LOG_ROUNDS = 11
    MONGODB_SETTINGS = {
        "db": os.getenv("MONGODB_NAME", "sloovi"),
        "host": os.getenv("MONGODB_URI"),
    }


@dataclass
class TestingConfig(Config):
    TESTING = True
    MONGODB_SETTINGS = {
        "db": os.getenv("MONGODB_NAME", "sloovi"),
        "host": os.getenv("MONGODB_TEST_URI"),
    }
    BCRYPT_LOG_ROUNDS = 4


@dataclass
class DevelopmentConfig(Config):
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4


@dataclass
class ProductionConfig(Config):
    PRODUCTION = True


config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
}
