from django.db import models

# Create your models here.
from pygments.styles import get_all_styles
from pygments.lexers import get_all_lexers
from django.db.models import *

LEXERS =  [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0],item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item,item) for item in get_all_styles()])


class Snippets(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # title = models.
