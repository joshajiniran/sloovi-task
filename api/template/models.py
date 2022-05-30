import mongoengine as me
from api.auth.models import User


class Template(me.Document):
    template_name = me.StringField(required=True)
    subject = me.StringField(required=True)
    body = me.StringField()
    owner = me.ReferenceField(User, unique_with="template_name")

    def serialize(self):
        return {
            "_id": str(self.pk),
            "template_name": self.template_name,
            "subject": self.subject,
            "body": self.body,
            "owner": str(self.owner.pk),
        }
