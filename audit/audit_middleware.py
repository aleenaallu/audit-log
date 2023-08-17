import logging
from audit.models import APICall
# from user.User.UserLogin.models import UserLogin

logger = logging.getLogger(__name__)

class APILoggingMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("hello audit")
        # Process the request and get the response
        response = self.get_response(request)
        user = request.user
        print("==================")
        print(request.META)
        # print(user.META)
        extra_json={
                    "device_name":request.META['REMOTE_ADDR'],
                    "USERNAME":request.META['USERNAME'],
                    "USERPROFILE":request.META['USERPROFILE'],
                    "USERDOMAIN":request.META['USERDOMAIN'],
                    "SERVER_SOFTWARE":request.META['SERVER_SOFTWARE'],
                    "SERVER_NAME":request.META['SERVER_NAME'],
                    "REQUEST_METHOD":request.META['REQUEST_METHOD'],
                    "SCRIPT_NAME":request.META['SCRIPT_NAME'],
                }
        
                
        # Log and store API call details
        if user.is_authenticated and request.path.startswith('/api/'):
            
            
            # Create a new APICall object with relevant information
            try:
                user_login = user.username
            except user.DoesNotExist:
                user.objects.create(user=user)

            api_call = APICall(
                user=request.user,
                endpoint=request.path,
                method=request.method,
                ip_address=request.META['REMOTE_ADDR'],
                extra_data=extra_json
            )
            
            
            # Save the API call to the database
            api_call.save()

            # Log the API call details using the logger
            logger.info(f"API call by user: {request.user.username}, Endpoint: {request.path}, Method: {request.method}, IP Address: {request.META['REMOTE_ADDR']}")

        # Retrieve and process API calls made by the user
        if user.is_authenticated:
            # Get all API calls made by the user
            user_api_calls = self.get_user_api_calls(request.user)

            # Iterate over the API calls
            for api_call in user_api_calls:
                # Access the details of each API call
                endpoint = api_call.endpoint
                method = api_call.method
                ip_address = api_call.ip_address

                # Do something with the API call details
                print(f"Endpoint: {endpoint}, Method: {method}, IP Address: {ip_address}")

        # Return the response
        return response
    
    def get_user_api_calls(self, user):
        # Retrieve all API calls made by the user
        api_calls = APICall.objects.filter(user=user)
        return api_calls
