from django.contrib import admin

from .models import User, FrequenceList, RapportInfo, Rapport

admin.site.register(User)
admin.site.register(FrequenceList)
admin.site.register(RapportInfo)
admin.site.register(Rapport)