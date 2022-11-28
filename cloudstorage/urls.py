"""hybridcloud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp_views
from proxyapp import views as proxyapp_views
from controllerapp import views as controllerapp_views
from clientapp import views as clientapp_views
from django.conf.urls.static import static
from django.conf import settings
# from mysite.core import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # mainapp
    path('',mainapp_views.main_home,name='main_home'),
    path('main-about',mainapp_views.main_about,name='main_about'),
    path('main-contact',mainapp_views.main_contact,name='main_contact'),

    # proxyapp
    path('main-proxy-login',proxyapp_views.main_proxy_login,name='main_proxy_login'),
    path('proxy-home',proxyapp_views.proxy_home,name='proxy_home'),
    path('proxy-storage-analysis',proxyapp_views.proxy_storage_analysis,name='proxy_storage_analysis'),
    path('accepted-uploaded-file/<int:id>/',proxyapp_views.accept_uploaded_file,name="accepted_uploaded_file"),
    path('declined-uploaded-file/<int:id>/',proxyapp_views.decline_uploaded_file,name="declined_uploaded_file"),
    path('proxy-transfer-request',proxyapp_views.proxy_transfer_request,name='proxy_transfer_request'),
    
    # controllerapp
    path('main-controller-login',controllerapp_views.main_controller_login,name='main_controller_login'),
    path('controller-home',controllerapp_views.controller_home,name='controller_home'),
    path('controller-all-users',controllerapp_views.controller_all_users,name='controller_all_users'),
    path('controller-filesystem-request',controllerapp_views.controller_filesystem_request,name='controller_filesystem_request'),
    path('controller-graphical-analysis',controllerapp_views.controller_graphical_analysis,name='controller_graphical_analysis'),

    path('controller-user-details',controllerapp_views.controller_user_details,name='controller_user_details'),
    path('accepted-client/<int:id>/',controllerapp_views.accept_clients,name="accepted_client"),
    path('declined-client/<int:id>/',controllerapp_views.decline_clients,name="declined_client"),
    # path('accepted_uploaded_files/<int:id>/',controllerapp_views.accept_uploaded_files,name="accepted_file"),
    # path('declined_uploaded_files/<int:id>/',controllerapp_views.decline_uploaded_files,name="declined_file"),
    path('accepted_uploaded_file_transfer/<int:id>/',controllerapp_views.accept_uploaded_file_transfer_request,name="accepted_uploaded_file_transfer"),
    path('declined_uploaded_file_transfer/<int:id>/',controllerapp_views.decline_uploaded_file_transfer_request,name="declined_uploaded_file_transfer"),
    

    # clientapp
    path('main-client-register',clientapp_views.main_client_register,name='main_client_register'),
    path('main-client-login',clientapp_views.main_client_login,name='main_client_login'),
    path('client-home',clientapp_views.client_home,name='client_home'),
    path('client-myfiles',clientapp_views.client_myfiles,name='client_myfiles'),
    path('client-myprofile',clientapp_views.client_myprofile,name='client_myprofile'),
    path('client-upload',clientapp_views.client_upload,name='client_upload'),
    # path('client-file-transfer-request/<int:id>/',clientapp_views.file_transfer_request,name='client_file_transfer_request'),
    path('demo/<int:id>/',clientapp_views.demo,name='demo'),
    path('client-file-request/<int:id>/',clientapp_views.file_transfer_request,name='client_file_request'),
    # path('get_context_data',clientapp_views.get_context_data,name='get_context_data'),

  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
