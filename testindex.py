__author__ = 'rudragouda'

from mongoengine import *
connect("testingindex")
import uuid


class JobMailcol(DynamicDocument):
    identifier = StringField(required=True, unique=True, primary_key=True)
    mailId = StringField()
    companyId = StringField(required=True)
    candidateEmail = EmailField(required=True)
    positionId = StringField(required=True)

    meta = {
        'indexes': [{
            'fields': ["companyId", "positionId", "candidateEmail"],
            'unique': True
            }]
    }

jm = JobMailcol()
jm.identifier = str(uuid.uuid4())
jm.mailId = "tgfv"
jm.companyId = "1111"
jm.candidateEmail = "rudra.gouda@edgenetworks.in"
jm.positionId = "abcd"
jm.save()
