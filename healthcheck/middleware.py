class ProbeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check if the request is coming from a Kubernetes probe by its IP or other identifiable headers
        if request.path == "/healthcheck/":
            # Skip ALLOWED_HOSTS check for probe requests
            return self.get_response(request)

        return self.get_response(request)
