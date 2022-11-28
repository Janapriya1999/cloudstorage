from django.shortcuts import render

# Create your views here.
def main_home(request):
    return render(request,"mainapp/main-home.html")
def main_about(request):
    return render(request,"mainapp/main-about.html")
def main_contact(request):
    return render(request,"mainapp/main-contact.html")
def main_client_register(request):
    return render(request,"mainapp/main-client-register.html")
def main_client_login(request):
    return render(request,"mainapp/main-client-login.html")
def main_proxy_login(request):
    return render(request,"mainapp/main-proxy-login.html")
def main_controller_login(request):
    return render(request,"mainapp/main-controller-login.html")