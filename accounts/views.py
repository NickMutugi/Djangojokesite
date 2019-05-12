from django.shortcuts import render
from .models import Contacts
import requests,json

def home(request):
    if request.method=='POST':
        firstname=request.POST.get('fname')
        lastname=request.POST.get('lname')

        r=requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName='+ lastname)
        json_data= json.loads(r.text)
        joke=json_data.get('value').get('joke')

        context={'joker' : joke}
        return render(request,'accounts/homepage.html',context)
    else:
        firstname='Nick'
        lastname='Mutugi'

        r=requests.get('http://api.icndb.com/jokes/random?firstName=' + firstname + '&lastName='+ lastname)
        json_data= json.loads(r.text)
        joke=json_data.get('value').get('joke')

        context={'joker' : joke}

        return render(request,'accounts/homepage.html')


def portfolio(request):
    return render(request,'accounts/portfolio.html')

def contacts(request):
    if request.method=='POST':
        emails=request.POST.get('email')
        subjects=request.POST.get('subject')
        messages=request.POST.get('message')


        c=Contacts(email=emails,subject=subjects,message=messages)
        c.save()

        return render(request,'accounts/thankyou.html')


    else:
        return render(request,'accounts/contacts.html')
