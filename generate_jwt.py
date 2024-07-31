import jwt
import datetime

# Define the payload for the JWT
payload = {
    'user_id': 1,  # User ID to be included in the token
    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),  # Token expiry time set to 1 day from now
}

# Define the secret key (should match the SECRET_KEY in settings.py)
secret = 'secret-key'

# Encode the payload to create a JWT
token = jwt.encode(payload, secret, algorithm='HS256')

# Print the generated token
print(token)
