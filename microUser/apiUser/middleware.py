from .tokenValidation.token_validate import tokenAnalyse
from django.http import HttpResponse
from .rapport.readRapport import ReadRapport, setReadRapport
from .tools.getURL import getJSON

HEADER_TOKEN = 'Token-User'

class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.setQueueListener()
    
    def setQueueListener(self):
        rapport = ReadRapport()
        setReadRapport(rapport)

    def __call__(self, request):
        if not request.path.startswith('/repos'):
            return self.get_response(request)

        result = tokenAnalyse(request, self)
        if result != None: # analyse le token et envoie une erreur s'il y a une invalidité
            return self.throwError(result)

        return self.get_response(request)


        
    
    def throwError(self, error):
        return HttpResponse("{\"error\": \"" + error.replace('"', '\"') + "\"}", content_type="application/json")