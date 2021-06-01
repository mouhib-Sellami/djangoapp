from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse

from .forms import *
import json
from .models import *
# Create your views here.
from django.core import serializers

def index(request):
    if request.method == 'POST':
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vetrine')
    else:
        form = ProduitForm()
        return render(request,'majProduits.html',{'form':form})
    
def shop(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('/magasin')
    else:
        form = CommandeForm()
        return render(request,'cammande.html',{'form':form})
        
        
def vetrine(request):
    listp = Produit.objects.all()
    return render(request,'vitrine.html',{'list':listp})

def forni(request):
    listf = Fournisseur.objects.all()
    return render(request,'fornisseur.html',{'list':listf})

def forniprod(request, id):
    forni = Fournisseur.objects.get(id=id)
    forniprod = Produit.objects.filter(fournisseur=forni)
    return render(request,'forniprod.html',{'list':forniprod})

def viewshop(request):
    com = Commander.objects.all()
    print(com)
    return render(request,'viewshop.html',{'com':com})

def deleteforni(request,id):
    forni = Fournisseur.objects.get(id=id)
    forni.delete()
    return redirect('forni')

def viewshopcart(request,id):
    pass
def addforni(request):
    if request.method == "POST":
        form = ForniForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('forni')
    else:
        form = ForniForm()
        return render(request,'addforni.html',{'form':form})

def deletecom(request,id):
    c = Commander.objects.filter(id = id).first()
    c.delete()
    return redirect('viewshop')