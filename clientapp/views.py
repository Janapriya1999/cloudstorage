from django.contrib import messages
from django.shortcuts import render,redirect,get_object_or_404
from clientapp.models import ClientModel, UploadDocumentModel, PrivateDocument
# S3 Setup
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.core.paginator import Paginator


from django.core.files.storage import FileSystemStorage

def client_home(request):
    
    return render(request,"clientapp/client-home.html")


def client_myfiles(request):
    client_id=request.session['client_id']
    clientdetails=ClientModel.objects.get(client_id=client_id)
    # documents = PrivateDocument.objects.filter(video_uploader=client_id).all()
    
   
    fPosts=PrivateDocument.objects.filter(video_uploader=client_id).all().order_by('-video_uploader')
    paginator = Paginator(fPosts, 5)

    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

    for i in post:
        print(i.random_id,'fffff')
    
    return render(request,"clientapp/client-myfiles.html",{'post':post})



class DocumentCreateView(CreateView):
   model = UploadDocumentModel
   fields = ['uploaded_video_file', ]
   success_url = reverse_lazy('home')


def client_upload(request):
    client_id=request.session['client_id']
    profile=ClientModel.objects.get(client_id=client_id)
    print(profile)

    if request.method == "POST" and request.FILES["video"]:
        name=request.POST.get("name")
        video=request.FILES["video"]
        a=video.size
        a1=a/1000000 
        # bytes to kb convertion
        print(a,'nine')
        print(a1,'ten')

        print(video.name,'kkkkk')
        message=request.POST.get("message")
        
        
        
        if a1 >= 1:
            p1=PrivateDocument.objects.create(
                upload_file_name=name,
                uploaded_video_file=video,
                upload_message=message,
                video_uploader=profile,
                s3_files=a1,
                efs_file=0)
        else:
            p1=PrivateDocument.objects.create(
                upload_file_name=name,
                uploaded_video_file=video,
                upload_message=message,
                video_uploader=profile,
                s3_files=0,
                efs_file=a1)

        
        try:
            print('one')
            
            file_name = video.name
            print(file_name,'gggg')

            my_file = open(file_name, 'w', encoding='utf-8')

            my_file.write('first line' + '\n')
            my_file.write('second line' + '\n')
            my_file.write('third line' + '\n')
            fs = FileSystemStorage()
            print('two')
            fs.save('uploads/'+file_name, video)

            my_file.close() # 👈️  manually close file

            print('three')
        except Exception as e:
            print(e)
            print('error')
        
        if p1:
            messages.success(request,"Successfully Video Uploaded")
        else:
            messages.error(request,"Product Not Uploaded, Please try again")
        return redirect('client_upload')
    
    return render(request,"clientapp/client-upload.html")

def client_myprofile(request):
    client_id=request.session['client_id']
    x = ClientModel.objects.get(client_id=client_id)
    if request.method == "POST":
        fullname=request.POST.get("fullname")
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        password=request.POST.get("password")
        
        print(fullname,contact,email,password)
        
        
        x.client_email=email
        x.client_password=password
        x.client_contact=contact
        x.client_fullname=fullname
        
        x.save()
        if x:
            messages.success(request,"successfully updated")
        else:
            messages.error(request,"Details Not Updated,Please Check Credentials Again & Update")
        return redirect("client_myprofile")
    return render(request,"clientapp/client-myprofile.html",{'x':x})


def main_client_register(request):
    if request.method == "POST" and request.FILES["photo"]:
        fullname=request.POST.get("fullname")
        contact=request.POST.get("contact")
        email=request.POST.get("email")
        password=request.POST.get("password")
        photo=request.FILES["photo"]
        
        print(fullname,contact,email,password,photo)

        client_data = ClientModel.objects.create(client_fullname=fullname,client_contact=contact,client_email=email,client_password=password,client_photo=photo)
        client_data.save()
        

        try:
            print('one')
            
            file_name = photo.name
            print(file_name,'photo')

            my_file = open(file_name, 'w', encoding='utf-8')

            my_file.write('first line' + '\n')
            my_file.write('second line' + '\n')
            my_file.write('third line' + '\n')
            fs = FileSystemStorage()
            print('two')
            fs.save('uploads/'+file_name, photo)

            my_file.close() # 👈️  manually close file

            print('three')
        except Exception as e:
            print(e)
            print('error')
        
        if client_data:
            messages.success(request,"successfully registered")
            return redirect('main_client_login')
        else:
            messages.error(request,"Your form is not registered, please try again")
        # return redirect('main_client_login')
        

    return render(request,"mainapp/main-client-register.html")


def main_client_login(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")

        try:
            check = ClientModel.objects.get(client_email=email,client_password=password)
            request.session['client_id']=check.client_id
            print(check)

            if check.client_status == 'accepted':
                messages.success(request,'Successfully Login')
                return redirect('client_home')
                
            elif check.client_status == 'pending':
                messages.warning(request,'Your request is in pending, please wait for until acceptance')
            elif check.client_status == 'rejected':
                messages.error(request,'Your request is rejected, so you cannot login')
        except:
                messages.info(request,'invalid login')
    return render(request,"mainapp/main-client-login.html")


def file_transfer_request(request,id):
    print('ccc')
    client_id=request.session['client_id']
    client=ClientModel.objects.get(client_id=client_id)
    rec=PrivateDocument.objects.get(upload_file=id)
    rec.transfer_status = "requested"
    rec.save()

    # rec.upload_file_transfer_status = "transfer"
    # # rec.upload_file_transfer_status="requested"
    # rec.save()
    # # obj2=get_object_or_404(PrivateDocument,upload_file=id)
    # # obj2.transfer_status = 'processing'
    # # obj2.upload_file_transfer_status='processing'
    
    # # obj2.save()
    
    
    return redirect("client_myfiles")

def demo(request,id):
    print(id,'kkkk')

    return render(request,"clientapp/client-home.html")
