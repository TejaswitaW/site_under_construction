from django.shortcuts import HttpResponse,render


class SiteUnderConstructionMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self,request):
        # print("Call From Middleware Before View")
        # response = HttpResponse("This Site is Under Construction")
        response = render(request,'mysite/siteuc.html')
        # print("Call From Middleware After View")
        return response