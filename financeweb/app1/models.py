from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Expense(models.Model):
	ename = models.CharField(max_length=50)
	eamount = models.IntegerField(max_length=20, blank=False)
	def __unicode__(self):
		return unicode(self.ename)


class Gprofit(models.Model):
	pamount = models.IntegerField(max_length=20, blank=False)
	def __unicode__(self):
		return unicode(self.pamount)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    companyname = models.CharField(max_length=200)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Project(models.Model):
	pname = models.CharField(max_length=30)
	exp = models.ManyToManyField(Expense)
	prof = models.ForeignKey(Gprofit)
	client = models.ForeignKey(UserProfile)
	def __unicode__(self):
		return unicode(self.pname)



