from ..tools.getURL import getJSON

URL_QUERY = 'http://127.0.0.1:3000/api/exist/token/'

def isToken_valid(token): # vérifie si le token-user passé en paramètre est correct
    global URL_QUERY
    result = getJSON(URL_QUERY + token)
    return not ('exist' in result.keys()) or result['exist']
