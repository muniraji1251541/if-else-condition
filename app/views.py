from django.shortcuts import render

# Create your views here.

def num(request):
    d={'a':20,'b':50}
    return render(request,'num.html',d)