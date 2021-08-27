from django.contrib import admin

from .models import Mirror, Production, Another, Color, Manufacture

admin.site.register(Manufacture)
admin.site.register(Color)
admin.site.register(Mirror)
admin.site.register(Another)
admin.site.register(Production)
