from mail_factory import factory
from app1.models import *
from django.contrib.auth.models import User
from mail_factory.mails import BaseMail
from mail_factory.contrib.auth.mails import PasswordResetMail


class WelcomeEmail(BaseMail):
    template_name = 'activation_email'
    params = ['user', 'site_name', 'site_url']

factory.register(WelcomeEmail)

factory.register(PasswordResetMail)

