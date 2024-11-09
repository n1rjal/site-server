from django.http.response import JsonResponse


def health_check(request):
    return JsonResponse(
        {
            "ok": 200,
        }
    )
