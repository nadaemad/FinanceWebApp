# Import the UserProfile model individually.
from app1.models import UserProfile, Expense, Gprofit, Project, Revenue
from django.contrib import admin

admin.site.register(Expense)
admin.site.register(Gprofit)
admin.site.register(Project)
admin.site.register(Revenue)
admin.site.register(UserProfile)

# Register your models here.
