from hmac import compare_digest

import mongoengine as me


class User(me.Document):
    first_name = me.StringField(max_length=50)
    last_name = me.StringField(max_length=50)
    email = me.EmailField(required=True, unique=True)
    password = me.StringField(required=True)

    def check_password(self, password):
        return compare_digest(self.password, password)

    def serialize(self):
        return {
            "_id": str(self.pk),
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
        }
