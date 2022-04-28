from django.conf import settings
from django.contrib import admin
from django.core.validators import MinLengthValidator

from django.db import models

from ads.models import Comment


class a(admin.ModelAdmin):
    pass


admin.site.register(Comment, a)
