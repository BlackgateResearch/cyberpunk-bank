from django.db import models

from uuid import uuid4


class Account(models.Model):
    account_id = models.CharField(max_length=5, default=lambda: str(uuid4())[:5])
    holder = models.CharField(max_length=30)
    balance = models.IntegerField(max_length=30)

    def __unicode__(self):
        return "%s: %s" % (str(self.holder), str(self.balance))
