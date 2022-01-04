from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Ami,Tumi
# Create your views here.
def index(req):
    #Select * From Ami Order by First name
    ami_list = Ami.objects.order_by('first_name')

    return render(req,'index.html',{'text_1':'I am a text sent from view.py','ami':ami_list})
def contact(req):
    return HttpResponse("<h1>HI It's Contact Page</h1>")
