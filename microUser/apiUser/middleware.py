from .tokenValidation.token_validate import tokenAnalyse
from django.http import HttpResponse
from .rapport.readRapport import ReadRapport
from .tools.getURL import getJSON

HEADER_TOKEN = 'Token-User'

RABBIT = {
    'URL': 'amqp://guest:Romain01@app.updatr.tech',
    'QUEUE': 'alert'
}

class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.setQueueListener()
    
    def setQueueListener(self):
        rapport = ReadRapport(RABBIT['URL'])
        rapport.listen(RABBIT['QUEUE'])

    def __call__(self, request):
        response = self.get_response(request)

        if not request.path.startswith('/repos'):
            return response

        return tokenAnalyse(request, response, self)
    
    def throwError(self, error):
        return HttpResponse("{\"error\": \"" + error.replace('"', '\"') + "\"}", content_type="application/json")