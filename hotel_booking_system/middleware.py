import logging
from django.http import JsonResponse, HttpResponse
from django.utils.deprecation import MiddlewareMixin

logger = logging.getLogger(__name__)

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

class AuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path in ['/', '/login', '/signup', '/admin/'] or request.path.startswith('/admin/'):
            return None
        token = request.headers.get('Authorization')
        logger.info(f'Token received: {token}')
        if token is None:
            logger.warning('No token provided')
            return JsonResponse({'error': 'Forbidden'}, status=403)
        if token != 'valid-token':
            logger.warning(f'Forbidden: Invalid token - Token: {token}')
            return JsonResponse({'error': 'Forbidden'}, status=403)
        logger.info('Token is valid')
        return None

class JsonResponseMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        if request.path.startswith('/api/'):  # Assuming API endpoints start with /api/
            if not isinstance(response, JsonResponse):
                try:
                    content = response.json()
                except (AttributeError, ValueError):
                    content = response.content.decode()
                response = JsonResponse({'data': content, 'status': response.status_code})
        return response
