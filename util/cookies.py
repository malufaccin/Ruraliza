NOME_COOKIE_AUTH = "jwt-token"

def adicionar_cookie_auth(response, token, dias=1):
    response.set_cookie(
        key=NOME_COOKIE_AUTH, 
        value=token, 
        max_age=24*3600*dias, 
        httponly=True, 
        samesite="lax")
    return response


def excluir_cookie_auth(response):
    response.set_cookie(
        key=NOME_COOKIE_AUTH, 
        value=" ",
        max_age=1,
        httponly=True, 
        samesite="lax")
    return response