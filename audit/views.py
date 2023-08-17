from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import APICall
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,AllowAny


# @login_required
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_api_calls(request):
    # Retrieve API calls made by the authenticated user, ordered by timestamp
    api_calls = APICall.objects.filter(user=request.user.id).order_by('-timestamp')

    # Prepare the response data
    response_data = {
        'api_calls': [
            {
                'endpoint': api_call.endpoint,
                'method': api_call.method,
                'timestamp': api_call.timestamp
            }
            for api_call in api_calls
        ]
    }

    # Return the response as JSON
    return JsonResponse(response_data)
