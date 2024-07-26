import jwt
import datetime

payload = {
    'user_id': 1,
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Token expiry time
}

secret = 'secret-key'  # Ensure this matches the SECRET_KEY in settings.py
token = jwt.encode(payload, secret, algorithm='HS256')
print(token)
