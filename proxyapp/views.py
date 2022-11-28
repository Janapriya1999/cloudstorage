from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from clientapp.models import PrivateDocument,ClientModel
from django.core.paginator import Paginator

# -random letter generator-
import string
import random
# import uuid
# Create your views here.
def proxy_home(request):
    x=ClientModel.objects.filter(client_status="pending").count()
    y=ClientModel.objects.filter(client_status="accepted").count()
    z=ClientModel.objects.filter(client_status="declined").count()
    p=PrivateDocument.objects.all().count()


    return render(request,"proxyapp/proxy-home.html",{'p':p,'x':x,'y':y,'z':z})

def proxy_storage_analysis(request):
    y=PrivateDocument.objects.all()
    for i in y:
        i.file_size = (i.uploaded_video_file.size)/1000000
    # y=PrivateDocument.objects.filter(video_uploader=id)
    # client=ClientModel.objects.get(pk=id)
    
    return render(request,"proxyapp/proxy-storage-analysis.html",{'y':y})

def proxy_transfer_request(request):
    # documents=PrivateDocument.objects.all()
    fPosts=PrivateDocument.objects.all().order_by('-upload_file')
    paginator = Paginator(fPosts, 4)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

    return render(request,"proxyapp/proxy-transfer-request.html",{'post':post})

def accept_uploaded_file(request,id):
    accept = get_object_or_404(PrivateDocument,upload_file=id)
    accept.upload_file_status = "accepted"
    accept.save(update_fields=["upload_file_status"])
    accept.save()
    
    # alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

    # n=3
    # apikey = ""
    # for i in range(n):
    #     apikey += alphabet[random.randint(0,25)]
    # print("" .join(random.sample(apikey, len(apikey))))
    if accept.upload_file_status == 'accepted':
        letters=string.ascii_letters
        a= ''.join(random.choice(letters) for i in range(16))
        print(a,'randomkey')
        accept.random_id = a
        accept.save()
    # if accept.upload_file_status == 'accepted':
    #     print ("The random id using uuid1() is : ",end="")
    #     code = uuid.uuid1()
    #     print(code,'coddddd')
    #     accept.random_id = code
    #     accept.save()
    # else:
    #     return redirect('proxy_transfer_request')
    
    return redirect('proxy_transfer_request')

def decline_uploaded_file(request,id):
    decline = get_object_or_404(PrivateDocument,upload_file=id)
    decline.upload_file_status = "declined"
    decline.save(update_fields=["upload_file_status"])
    decline.save()

    return redirect('proxy_transfer_request')

   
def main_proxy_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if username == "proxy" and password == "proxy":
            messages.success(request,'Successfully Login')
            return redirect('proxy_home')
        else:
            messages.warning(request,'invalid login')
            return redirect("main-proxy-login")
    return render(request, "mainapp/main-proxy-login.html")