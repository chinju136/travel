from django.contrib import admin
from .models import Demo
from .models import Place
admin.site.register(Place)
admin.site.register(Demo)