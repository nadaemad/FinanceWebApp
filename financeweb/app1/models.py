from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class LastSeen(object):

    def process_request(self, request):
        user = request.user
        if not user.is_authenticated(): return None  
        up = user.get_profile()
        up.last_seen_on = datetime.now()
        up.last_activity_ip = request.META['REMOTE_ADDR']
        up.save()
        return None

class Notification(models.Model):
	ntitle = models.CharField(max_length=50)
	nmessage = models.CharField(max_length=200)
	def __unicode__(self):
		return unicode(self.ntitle)

class Expense(models.Model):
	ename = models.CharField(max_length=50)
	eamount = models.IntegerField(blank=False)
	expense_date = models.DateField()
	def __unicode__(self):
		return unicode(self.ename)


class Gprofit(models.Model):
	pamount = models.IntegerField(blank=False)
	profit_date = models.DateField()
	def __unicode__(self):
		return unicode(self.pamount)


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, related_name='user_profile')

    # The additional attributes we wish to include.
    companyname = models.CharField(max_length=200)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Revenue(models.Model):
	revenue_name = models.CharField(max_length=50)
	revenue_amount = models.IntegerField(blank=False)
	revenue_date = models.DateField()
	def __unicode__(self):
		return unicode(self.revenue_name)


class Project(models.Model):
	pname = models.CharField(max_length=30)
	exp = models.ManyToManyField(Expense)
	prof = models.ForeignKey(Gprofit)
	revenues = models.ManyToManyField(Revenue)
	client = models.ForeignKey(UserProfile)
	def __unicode__(self):
		return unicode(self.pname)


class Post(models.Model):
	text = models.CharField(max_length=500)
	title= models.CharField(max_length=100)
	def __unicode__(self):
		return self.title


class comment(models.Model):
	comment = models.TextField()
	post = models.ForeignKey(Post)
	def __unicode__(self):
		return self.comment





