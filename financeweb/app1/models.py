from django.db import models

# Create your models here.


class user(models.Model):
	user_email = models.CharField(max_length=120,null=True, blank=False, unique=True)
	user_name = models.CharField(max_length=120,null=True, blank=False, unique=True)
	first_name = models.CharField(max_length=120, null=False, blank=False)
	Last_name = models.CharField(max_length=120, null=False, blank=False)
	password = models.CharField(max_length=120, null=False, blank=False)
	confirm_password = models.CharField(max_length=120, null=False, blank=False)
	company_name = models.CharField(max_length=200,null=False,blank=False, unique=True)
	company_date_of_origin = models.DateTimeField()

	def __unicode__(self):
		return unicode(self.first_name)



class Expense(models.Model):
	ename = models.CharField(max_length=50)
	eamount = models.IntegerField(max_length=20, blank=False)
	def __unicode__(self):
		return unicode(self.ename)


class Gprofit(models.Model):
	pamount = models.IntegerField(max_length=20, blank=False)
	def __unicode__(self):
		return unicode(self.pamount)


class Project(models.Model):
	pname = models.CharField(max_length=30)
	exp = models.ManyToManyField(Expense)
	prof = models.ForeignKey(Gprofit)
	def __unicode__(self):
		return unicode(self.pname)



