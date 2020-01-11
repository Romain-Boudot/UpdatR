from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers
from .viewSet import UserViewSet, FrequenceListSet, RapportInfoSet, RapportSet
from . import views

router = routers.DefaultRouter()
router.register(r'users', UserViewSet) # nous référencons les models pour l'API REST
router.register(r'frequencelist', FrequenceListSet)
router.register(r'rapportinfo', RapportInfoSet)
router.register(r'rapport', RapportSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
