from django.contrib import admin
from .models import Disk, Seal, Artist

admin.site.register(Disk)
admin.site.register(Seal)
admin.site.register(Artist)