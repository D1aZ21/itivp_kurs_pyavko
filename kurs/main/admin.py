from django.contrib import admin
from .models import TariffCategory, Tariff, AuthUser, Bookg

admin.site.register(TariffCategory)
admin.site.register(Tariff)
admin.site.register(AuthUser)
admin.site.register(Bookg)
