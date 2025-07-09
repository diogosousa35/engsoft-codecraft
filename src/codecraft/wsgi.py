"""
WSGI config for nexus project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexus.settings.production')

application = get_wsgi_application()
