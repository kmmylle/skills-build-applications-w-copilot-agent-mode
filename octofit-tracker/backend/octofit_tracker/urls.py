
import os
from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def api_root(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    api_url = f"https://{codespace_name}-8000.app.github.dev/api/"
    return JsonResponse({"api_root": api_url})

def activities_endpoint(request):
    codespace_name = os.environ.get('CODESPACE_NAME', 'localhost')
    url = f"https://{codespace_name}-8000.app.github.dev/api/activities/"
    return JsonResponse({"activities_url": url})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root),
    path('api/activities/', activities_endpoint),
]
