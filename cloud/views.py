from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from .forms import *
# Create your views here.
def login(request):
    if request.session.has_key("cloudId"):
        return redirect('home')
    else:
        if request.method == "POST":
            mail = request.POST['mail']
            print(mail)
            password = request.POST['password']
            q = User.objects.filter(email=mail, password=password).first()
            if q:
                request.session["cloudId"] = q.userId
                print("redirect")
                return redirect('home')
            else:
                messages.error(request, "E-mail or Password incorrect")
                return render(request, 'login.html')

    return render(request, 'login.html')

def register(request):
    if request.session.has_key("cloudId"):
        return redirect('home')
    else:
        if request.method == "POST":
            mail = request.POST['mail']
            password = request.POST['password']
            q = User.objects.filter(email=mail).first()
            if q:
                messages.error(request,"mail exist")
                return render(request,'register.html',{})
            else:
                user = User(email = mail,password=password)
                user.save()
                request.session['cloudId'] = user.userId
                return redirect('home')

    return render(request, 'register.html')

def index(request):
    return render(request,'cloud.html',{})



def home(request):
    if request.session.has_key('cloudId'):
        user = User.objects.filter(userId = request.session['cloudId']).first()
        Cloud = cloud.objects.filter(userId = user).all()
        print(Cloud)
        return render(request,'home.html',{'Cloud':Cloud})
    else:
        return redirect('login')

def viewfolder(request,id):
    if request.session.has_key('cloudId'):
        user = User.objects.filter(userId = request.session['cloudId']).first()
        folder = Folder.objects.filter(folderId = id).first()

        if request.method == "POST":
            files = request.FILES.getlist('files')
            list = []
            for f in files:
                file = File(userId=user, file=f)
                file.save()
                folder.files.add(file)
            messages.success(request,'Files added succesfully')
            new = Folder.objects.filter(folderId=id).all()
            return render(request,'viewfolder.html',{'Folder':new})
        else:
            return render(request,'viewfolder.html',{'Folder':folder})
    else:
        return redirect('login')

def addfolder(request):
    if request.session.has_key('cloudId'):
        user = User.objects.filter(userId = request.session['cloudId']).first()
        if request.method =='POST':
            name = request.POST['name']
            files = request.FILES.getlist('files')
            print(files)
            list = []
            for f in files:
                file = File(userId=user,file =f)
                file.save()
                list.append(file)
            nb = Folder.objects.all().count()
            folder = Folder(userId=user,name = name)
            folder.save()
            print(folder)
            for f in list:
                folder.files.add(f)
            c = Content(folder=folder)
            c.save()
            Cloud = cloud(userId=user,content=c)
            Cloud.save()

            return redirect('home')
        else:
            return render(request, 'addfolder.html')
    else:
        return redirect('login')

def addfile(request):
    if request.session.has_key('cloudId'):
        user = User.objects.filter(userId=request.session['cloudId']).first()
        if request.method =="POST":
            files = request.FILES.getlist('files')
            for f in files:
                file = File(userId=user,file =f)
                file.save()
                c = Content(file=file)
                c.save()
                Cl = cloud(userId=user,content=c)
                Cl.save()
            return redirect('home')

        else:
            return render(request,'addfile.html')
    else:
        return redirect('login')

def logout(request):
    if not request.session.has_key('cloudId'):
        return redirect ('login')
    try:
        del request.session['cloudId']
        return redirect('login')
    except:
        pass

def deletecontent(request):
    if request.session.has_key('cloudId'):
        user = User.objects.filter(userId = request.session['cloudId']).first()
        Cloud = cloud.objects.filter(userId = user).all()
        print(Cloud)
        return render(request,'delete.html',{'Cloud':Cloud})
    else:
        return redirect('login')
    
def deletefolder(request,id):
    if request.session.has_key('cloudId'):
        folder = Folder.objects.filter(folderId = id).first()
        folder.delete()
        return redirect('deletecontent')
    else:
        return redirect('login')    

def deletefile(request,id):
    if request.session.has_key('cloudId'):
        filee = File.objects.filter(fileId = id).first()
        filee.delete()
        return redirect('deletecontent')
    else:
        return redirect('login')    