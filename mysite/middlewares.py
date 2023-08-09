from django.shortcuts import HttpResponse


class SiteUnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        # print("Call From Middleware Before View")
        response = HttpResponse("This site is under construction,Please visit after some time.")
        # print("Call From Middleware After View")
        return response