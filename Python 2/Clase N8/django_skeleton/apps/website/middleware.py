from django.http import HttpResponseNotFound
from django.utils.deprecation import MiddlewareMixin
from django.conf import settings


class ProtectAdminMiddleware(MiddlewareMixin):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith("/admin"):
            if request.META["SERVER_PORT"] != '8000':
                return HttpResponseNotFound()

        return self.get_response(request)
