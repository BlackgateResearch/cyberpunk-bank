from django.db import models

class Account(models.Model):
    holder = models.CharField(max_length=30)
    balance = models.IntegerField(max_length=30)

    def __unicode__(self):
        return "%s: %s" % (str(self.holder), str(self.balance))
