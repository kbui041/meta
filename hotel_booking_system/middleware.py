import logging
import jwt
from django.conf import settings
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

class SimpleUser:
    def __init__(self, payload):
        self.id = payload.get('user_id')
        self.is_active = True  # Mocking the is_active attribute

    def __str__(self):
        return f"User({self.id})"

class FaviconMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == '/favicon.ico':
            return HttpResponse(status=204)

class LoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        logger.info(f'{request.method} {request.path} - Headers: {request.headers}')

    def process_response(self, request, response):
        logger.info(f'{response.status_code} {response.reason_phrase}')
        return response

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in ['/', '/login', '/signup', '/admin/'] or request.path.startswith('/admin/'):
            return None
        token = request.headers.get('Authorization')
        if token is None:
            logger.warning('No token provided')
            return JsonResponse({'error': 'Forbidden'}, status=403)
        try:
            # Remove 'Bearer ' from the token string
            token = token.split(' ')[1]
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user = SimpleUser(payload)  # Create a user-like object
            logger.info('Token is valid')
        except jwt.ExpiredSignatureError:
            logger.warning('Expired token')
            return JsonResponse({'error': 'Token has expired'}, status=403)
        except jwt.InvalidTokenError:
            logger.warning('Invalid token')
            return JsonResponse({'error': 'Invalid token'}, status=403)

class JsonResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith('/api/'):  # Assuming API endpoints start with /api/
            if not isinstance(response, JsonResponse):
                try:
                    # Attempt to parse the response content to JSON
                    content = response.json()
                except (AttributeError, ValueError):
                    content = response.content.decode()
                response = JsonResponse(content, safe=False)  # Return raw JSON content
        return response
