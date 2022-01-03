from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def index(req):
    diction = {'text_1':'I am a text sent from view.py'},
    return render(req,'index.html',{'text_1':'I am a text sent from view.py'})
def contact(req):
    return HttpResponse("<h1>HI It's Contact Page</h1>")
