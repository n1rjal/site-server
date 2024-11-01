from django.http.response import JsonResponse


# Create your views here.
def health_check():
    return JsonResponse({"status": "ok"})
