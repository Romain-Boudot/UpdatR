from .tokenValidation.token_validate import isToken_valid
from django.http import HttpResponse
from .rapport.readRapport import ReadRapport
from .tools.getURL import getJSON

HEADER_TOKEN = 'Token-User'

RABBIT = {
    'URL': 'amqp://guest:Romain01@app.updatr.tech',
    'QUEUE': 'alert'
}

USER_DATA_URL = 'http://127.0.0.1:3000/api/get/'

class Middleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.setQueueListener()
    
    def setQueueListener(self):
        rapport = ReadRapport(RABBIT['URL'])
        rapport.listen(RABBIT['QUEUE'])

    def __call__(self, request):
        headers = request.headers

        if not HEADER_TOKEN in headers.keys():
            return self.throwError('no token in header (specify by \'Token-User\' attribute in header)')

        token = headers[HEADER_TOKEN]

        if not isToken_valid(token):
            return self.throwError('Token invalid') # si le token n'est pas valide, nous envoyons une erreur
        
        user_data = getJSON(USER_DATA_URL + token)
        username = user_data['user']['preferred_username']
        session = request.session
        session['username'] = username
        test = session['username']
        response = self.get_response(request)

        return response
    
    def throwError(self, error):
        return HttpResponse("{\"error\": \"" + error.replace('"', '\"') + "\"}", content_type="application/json")