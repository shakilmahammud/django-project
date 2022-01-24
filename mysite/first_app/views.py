from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Ami,Tumi
from first_app.forms import Userform
# Create your views here.
def index(req):
    #Select * From Ami Order by First name
    ami_list = Ami.objects.order_by('first_name')
    return render(req,'index.html',{'text_1':'I am a text sent from view.py','ami':ami_list})
def form(req):
    nform =Userform()
    diction ={'Form':nform}
    if req.method == 'POST':
        nform = Userform(req.POST)
        diction.update({'Form':nform})
        if nform.is_valid():
            diction.update({'user_name':'field match'})
            diction.update({'email':'email match'})
            diction.update({'submit':'Yes'})
   
    return render(req,'form.html',context=diction)
    
