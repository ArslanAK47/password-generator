from django.shortcuts import render
from django.http import HttpResponse
import random

from django.utils.regex_helper import Choice
# Create your views here.

def home(request):
    return render(request, 'generator/home.html')

def password(request):

    mypassword = ""
    st = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
            st.extend(list('QWERTYUIOPASDFGHJKLZXCVBNM'))
    if request.GET.get('special'):
            st.extend(list('?@$%*&'))
    if request.GET.get('special'):
            st.extend(list('123456890'))

    length = int(request.GET.get('length'))

    
        
    for i in range(length):
        mypassword += random.choice(st)

    return render(request, "generator/password.html", {"password":mypassword})

def aboutus(request):
    return render(request, 'generator/aboutus.html')