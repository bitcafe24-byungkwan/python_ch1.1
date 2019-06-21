from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def hello(request):
    return render(request, 'helloworld/hello.html')


def hello2(requst, id=0):
    return HttpResponse(f'id:{id}')


def hello3(request):
    jsonresult = {
        'result': 'success',
        'data': ['hello', 1, 2, True, ('a', 'b', 'c')]
    }

    return JsonResponse(jsonresult)

