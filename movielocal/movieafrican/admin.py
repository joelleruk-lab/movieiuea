from django.contrib import admin
from .models import Movies,Series,Season,Episode

admin.site.register(Movies)
admin.site.register(Series)
admin.site.register(Season)
admin.site.register(Episode)

# Register your models here.
