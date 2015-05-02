
#for gmail or google apps
EMAIL_USE_TLS = True 
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'financewebapp@gmail.com'
EMAIL_HOST_PASSWORD = 'financialmonkeys'
EMAIL_PORT = 587


"""factory.mail('activation_email', [user.email],
             {'user': user,
              'site_name': settings.SITE_NAME,
              'site_url': settings.SITE_URL})"""