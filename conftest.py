import os
import sys
import django
from django.conf import settings

# Adiciona a raiz do projeto ao path
sys.path.insert(0, os.path.dirname(__file__))

# Configura Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
