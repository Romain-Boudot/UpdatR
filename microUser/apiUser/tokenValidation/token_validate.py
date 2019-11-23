from ..tools.getURL import getJSON

URL_QUERY = 'http://127.0.0.1:3000/api/exist/token/'

def isToken_valid(token):
    global URL_QUERY
    return getJSON(URL_QUERY + token)