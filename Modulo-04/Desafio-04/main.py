import jwt
from time import time  # Para gerar o timestamp da validade do token


def create_token(data, secret, user_id=123):

    payload = {
        'uid': user_id,
        'exp': int(time()) + 300,  # determina a validade do token em 5 minutos
        'language': data['language']
    }

    return jwt.encode(payload, secret, algorithm='HS256')


def verify_signature(token):

    secret = 'acelera'

    try:
        data = jwt.decode(token, secret, algorithm='HS256')
    except jwt.ExpiredSignatureError:
        print('Seu token esta expirado!')
    except jwt.InvalidSignatureError:
        return {"error": 2}
    except:
        print('Outro erro!')
    else:
        return data['language']  # Python
