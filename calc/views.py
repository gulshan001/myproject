from django.shortcuts import render
from django.http import HttpResponse
import math


# Create your views here.

def index(request):
    return render(request, 'index.html')


def logEvaluate(request):
    a=float(request.POST['a'])
    b=float(request.POST['b'])
    if a <0 or b<0 :
        message="You can not enter value which is less than 0 or negative!"
        return render(request, 'index.html', {'result': message})
    elif a==0 :
        message="Log value can not be calculated on 0"
        return render(request, 'index.html', {'result': message})

    elif b==0 :
        message="Base cannot be 0"
        return render(request, 'index.html', {'result': message})
    else:
        c=math.log(a,b)
        return render(request,'index.html', {'result': c})

