from django.http import HttpResponse

def helloworld(request):
    html = '<html><body><h1>HelloWorld!</h1></body></html>'
    return HttpResponse(html)
