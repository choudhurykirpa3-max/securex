from config import API_KEY

def validate_api_key(request):
    return request.headers.get("x-api-key") == API_KEY

