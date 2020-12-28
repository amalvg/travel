from django.contrib import admin
from .models import place, special, news

# Register your models here.
admin.site.register(place)
admin.site.register(special)
admin.site.register(news)