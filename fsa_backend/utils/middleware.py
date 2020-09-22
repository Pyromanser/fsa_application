from django.middleware.common import CommonMiddleware


class CustomCommonMiddleware(CommonMiddleware):

    def should_redirect_with_slash(self, request):
        # api should not be redirected
        if request.path_info.startswith("/api") and not request.path_info.startswith("/api/swagger"):
            return False
        return super().should_redirect_with_slash(request)
