from django.http import HttpResponse
def hello(request):
    return HttpResponse("Hello world %s %s %s" % (request.path, request.get_host(), request.get_full_path()))
