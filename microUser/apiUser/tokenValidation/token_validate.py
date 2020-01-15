from ..tools.getURL import getJSON
# import jwt

# URL_QUERY = 'http://127.0.0.1:3000/api/exist/token/'

TOKEN = {
    'HEADER': 'authorization',
    'GET': 'token'
}

USER_DATA_URL = 'http://127.0.0.1:3000/local/token/info/'

def tokenAnalyse(request, middleware):
    headers = request.headers
    params = request.GET
    if not (TOKEN['HEADER'] in headers.keys() or "'" + TOKEN['GET'] + "'" in params):
        return 'no token in header (specify by \'authorization\' attribute in header)'
        # return middleware.throwError('no token in header (specify by \'Token-User\' attribute in header)')
    
    token = None
    if TOKEN['HEADER'] in headers.keys():
        token = headers[TOKEN['HEADER']]
    if "'" + TOKEN['GET'] + "'" in params:
        token = params.get(TOKEN['GET'])

    if not token:
        return 'no token provided'

    # if token == None or not isToken_valid(token):
    #     return 'Token invalid'
        # return middleware.throwError('Token invalid') # si le token n'est pas valide, nous envoyons une erreur
    
    user_data = getJSON(USER_DATA_URL + token)
    if not user_data['valid']:
        return 'Token invalid'
        # return middleware.throwError(user_data['error'])

    username = user_data['username']
    session = request.session
    session['username'] = username
    return None

# def isToken_valid(token): # vérifie si le token-user passé en paramètre est correct
#     global URL_QUERY
#     result = getJSON(URL_QUERY + token)
#     return not ('exist' in result.keys()) or result['exist']
