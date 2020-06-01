from jwt import InvalidSignatureError, encode, decode


segredo = 'acelera'


def create_token(data, secret):
  return encode(data, secret)


def verify_signature(token):
  try:
    return decode(token, segredo)
  except InvalidSignatureError:
    return {"error": 2}
