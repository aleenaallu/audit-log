from django.urls import path
from audit.views import user_api_calls

urlpatterns = [
    path('api/', user_api_calls, name='user_api_calls'),
]
