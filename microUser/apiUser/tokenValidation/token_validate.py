from ..tools.getURL import getJSON
import jwt

URL_QUERY = 'http://127.0.0.1:3000/api/exist/token/'

TOKEN = {
    'HEADER': 'Token-User',
    'GET': 'token'
}

USER_DATA_URL = 'http://127.0.0.1:3000/api/get/'

def tokenAnalyse(request, response, middleware):
    headers = request.headers
    params = request.GET
    if not TOKEN['HEADER'] in headers.keys() and "'" + TOKEN['GET'] + "'" in params:
        return middleware.throwError('no token in header (specify by \'Token-User\' attribute in header)')
    
    token = None
    if TOKEN['HEADER'] in headers.keys():
        token = headers[TOKEN['HEADER']]
    else:
        token = params.get(TOKEN['GET'])

    if token == None or not isToken_valid(token):
        return middleware.throwError('Token invalid') # si le token n'est pas valide, nous envoyons une erreur
    
    user_data = getJSON(USER_DATA_URL + token)
    if 'error' in user_data:
        return middleware.throwError(user_data['error'])

    username = user_data['user']['preferred_username']
    session = request.session
    session['username'] = username
    response = middleware.get_response(request)

    return response

def isToken_valid(token): # vérifie si le token-user passé en paramètre est correct
    global URL_QUERY
    result = getJSON(URL_QUERY + token)
    return not ('exist' in result.keys()) or result['exist']
