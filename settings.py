import django_heroku

ALLOWED_HOSTS = ['localhost', 'miboggle.herokuapp.com']

django_heroku.settings(locals())