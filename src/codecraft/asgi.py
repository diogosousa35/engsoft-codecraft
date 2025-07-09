"""
ASGI config for nexus project.
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nexus.settings.production')

application = get_asgi_application()
