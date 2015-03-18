"""
WSGI config for Dashbird project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""
import os

# We defer to a DJANGO_SETTINGS_MODULE already in the environment. This breaks
# if running multiple sites in the same mod_wsgi process. To fix this, use
# mod_wsgi daemon mode with each site in its own daemon process, or use
# os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Dashbird.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Serve static files using Python
from whitenoise.django import DjangoWhiteNoise
application = DjangoWhiteNoise(application)
