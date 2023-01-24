from django.shortcuts import render
from app1.models import *
# Create your views here.

def display_topics(request):
    data_set_of_Topics=Topics.objects.all()
    d={"topics_data":data_set_of_Topics}
    
    return render(request,'display_topics.html',d)
    

def display_webpages(request):
    data_set_of_Webpages=Webpages.objects.all()
    d={"webpages_data":data_set_of_Webpages}
    
    return render(request,'display_webpages.html',d)


def display_Acces_rec(request):
    data_set_of_Acces_rec=Acces_rec.objects.all()
    d={"webpages_data":data_set_of_Acces_rec}
    
    return render(request,'display_Acces_rec.html',d)