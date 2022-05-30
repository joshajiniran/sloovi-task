import datetime
import os
from dotenv import load_dotenv


load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY")
    DEBUG = False
    TESTING = False
    PRODUCTION = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_EXPIRES_ON = datetime.timedelta(days=1)
    MONGODB_SETTINGS = {
        "db": os.getenv("DB_NAME"),
        "host": os.getenv("DB_URL"),
    }


class TestingConfig(Config):
    TESTING = True


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    PRODUCTION = True


config = {
    "development": DevelopmentConfig(),
    "testing": TestingConfig(),
    "production": ProductionConfig(),
}
