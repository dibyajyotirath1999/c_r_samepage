from django.shortcuts import render
from .models import crdata

def cr(request):
    if request.method=="POST":
        crdata(
            fname=request.POST.get("fname"),
            lname=request.POST.get("lname"),
            course= request.POST.get("course"),
            fee=request.POST.get("fee"),
            sub1=request.POST.get("s1"),
            sub2=request.POST.get("s2"),
            sub3=request.POST.get("s3"),
            sub4=request.POST.get("s4"),
            ).save()
        table=crdata.objects.all()
        return render (request,"cr.html",{"table":table})
    else:
        table=crdata.objects.all()
        return render (request,"cr.html",{"table":table})
        

    

