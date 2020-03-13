from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    params={'password': 'abcdhdfdklfdk'}
    return render(request,'generator/index.html' ,params)

def about(request):
    return render(request,'generator/about.html')
def password(request):
    lenght=int(request.GET.get('lengthselect'))

    unique_password=''

    choices=list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        choices.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if request.GET.get('number'):
        choices.extend(list("0123456789"))
    if request.GET.get('special'):
        choices.extend(list("@$%^&*()"))

    for i in range(lenght):
        unique_password+=random.choice(choices)

    params={'password':unique_password}

    return render(request, 'generator/password.html',params)
