from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
num1 = 4
num2 = 5
num3 = num1 + num2

print(num3)

def home(req):
    return HttpResponse('hello world')
