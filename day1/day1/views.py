# from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    # return HttpResponse("First Route")
    return render(request,'home.html')
def aboutPage(request):
    # return HttpResponse("Second route")
    return render(request,'about.html')
