from .tokenValidation.token_validate import isToken_valid
from django.http import HttpResponse

HEADER_TOKEN = 'Token-User'

class TokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        headers = request.headers

        if not HEADER_TOKEN in headers.keys():
            return self.throwError('no token in header (specify by \'Token-User\' attribute in header)')

        if not isToken_valid(headers[HEADER_TOKEN]):
            return self.throwError('Token invalid') # si le token n'est pas valide, nous envoyons une erreur

        response = self.get_response(request)

        return response
    
    def throwError(self, error):
        return HttpResponse("{\"error\": \"" + error.replace('"', '\"') + "\"}", content_type="application/json")