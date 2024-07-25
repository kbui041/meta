# hotel_booking_system/middleware.py
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware
import logging
from django.http import JsonResponse

logger = logging.getLogger(__name__)

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        logger.info(f'{request.method} {request.path}')
        response = self.get_response(request)
        return response

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)

    def __call__(self, request):
        self.logger.info(f'Request to {request.path} with headers {request.headers}')
        if request.path in ['/', '/login', '/signup']:
            return self.get_response(request)
        token = request.headers.get('Authorization')
        self.logger.info(f'Token received: {token}')
        if token == 'valid-token':
            return self.get_response(request)
        self.logger.warning('Forbidden: Invalid token')
        return JsonResponse({'error': 'Forbidden'}, status=403)
    