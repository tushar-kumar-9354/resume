# core/middleware.py
from django.shortcuts import redirect

class VerifyUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and not request.user.is_active:
            return redirect('login')
        return self.get_response(request)