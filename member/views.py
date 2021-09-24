from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def member1(request):
    return render(request, 'member1.html')



def member2(request):
    return render(request, 'member2.html')



def member3(request):
    return render(request, 'member3.html')



def member4(request):
    return render(request, 'member4.html')