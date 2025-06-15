
from django.http.response import JsonResponse
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def healthView(request):
    return JsonResponse({"status": "success"})