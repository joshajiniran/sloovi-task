from hmac import compare_digest

import mongoengine as me
from flask import current_app as app
from main import bcrypt


class User(me.Document):
    first_name = me.StringField(max_length=50)
    last_name = me.StringField(max_length=50)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)
    
    @staticmethod
    def make_password(password):
        return bcrypt.generate_password_hash(password, app.config.get('BCRYPT_LOG_ROUNDS')).decode("utf-8")

    def serialize(self):
        return {
            "_id": str(self.pk),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
