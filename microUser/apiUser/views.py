from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import routers
from .viewSet import UserViewSet
from .tokenValidation.token_validate import isToken_valid

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

def api_analyse(request):
    # path = request.path
    valid = isToken_valid('a')
    return HttpResponse('valid: ' + str(valid['exist']))
