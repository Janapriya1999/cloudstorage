import os
from importlib.resources import files
from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from clientapp.models import ClientModel,UploadDocumentModel,PrivateDocument
from django.core.paginator import Paginator

# Create your views here.
def controller_home(request):
    x=ClientModel.objects.filter(client_status="pending").count()
    y=ClientModel.objects.filter(client_status="accepted").count()
    z=ClientModel.objects.filter(client_status="declined").count()
    p=PrivateDocument.objects.all().count()

    return render(request,"controllerapp/controller-home.html",{'p':p,'x':x,'y':y,'z':z})

def controller_filesystem_request(request):
    client_id=request.session['client_id']
    x=ClientModel.objects.get(client_id=client_id)
    
    
    fPosts=PrivateDocument.objects.exclude(transfer_status='not-transfer').order_by('-transfer_status')
    

    paginator = Paginator(fPosts, 4)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

    return render(request,"controllerapp/controller-filesystem-request.html",{'x':x,'post':post})

def accept_uploaded_file_transfer_request(request,id):
    accept = get_object_or_404(PrivateDocument,upload_file=id)
    accept.upload_file_transfer_status = "transfered"
    accept.transfer_status= 'transfered'
    # file = str(accept.uploaded_video_file)
    # os.remove('media/uploads/'+file)
    accept.s3_files = accept.efs_file
    accept.efs_file = 0
    accept.save()

    return redirect('controller_filesystem_request')

def decline_uploaded_file_transfer_request(request,id):
    decline = get_object_or_404(PrivateDocument,upload_file=id)
    decline.upload_file_transfer_status = "declined"
    decline.save(update_fields=["upload_file_transfer_status"])
    decline.save()

    return redirect('controller_filesystem_request')

def controller_graphical_analysis(request):
    y=PrivateDocument.objects.all()
    for i in y:
        i.file_size = (i.uploaded_video_file.size)/1000000
    # y=PrivateDocument.objects.filter(video_uploader=id)
    # client=ClientModel.objects.get(pk=id)

    return render(request,"controllerapp/controller-graphical-analysis.html",{'y':y})

def controller_user_details(request):
    # c1=ClientModel.objects.order_by("-client_id")
    # print(c1)
    fPosts=ClientModel.objects.order_by("-client_id")
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)


    return render(request,"controllerapp/controller-user-details.html",{'post':post})


def accept_clients(request,id):
    accept = get_object_or_404(ClientModel,client_id=id)
    accept.client_status = "accepted"
    accept.save(update_fields=["client_status"])
    accept.save()

    return redirect('controller_user_details')

def decline_clients(request,id):
    decline = get_object_or_404(ClientModel,client_id=id)
    decline.client_status = "declined"
    decline.save(update_fields=["client_status"])
    decline.save()

    return redirect('controller_user_details')

def controller_all_users(request):
    # c2=ClientModel.objects.filter(client_status="accepted").order_by('-client_id')
    
    fPosts=ClientModel.objects.filter(client_status="accepted").order_by('-client_id')
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)




    return render(request,"controllerapp/controller-all-users.html",{'post':post})
    
def main_controller_login(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        if username == "controller" and password == "controller":
            messages.success(request,'Successfully Login')
            return redirect('controller_home')
        else:
            messages.warning(request,'invalid login')
            return redirect("main_controller_login")
    return render(request, "mainapp/main-controller-login.html")