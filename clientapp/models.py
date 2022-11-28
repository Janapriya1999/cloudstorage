from django.db import models
from django.conf import settings
# from django.contrib.auth.models import User
from cloudstorage.storage_backends import PrivateMediaStorage
from django.core.files.storage import FileSystemStorage

# Create your models here
class ClientModel(models.Model):
  client_id=models.AutoField(primary_key=True)
  client_fullname=models.CharField(max_length=100)
  client_contact=models.CharField(max_length=10)
  client_email=models.EmailField(max_length=100)
  client_password=models.CharField(max_length=100)
  client_photo=models.FileField(upload_to='uploads/',null = True)
  client_status=models.CharField(default="pending",max_length=50)
  class Meta:
    db_table='client_details'

class UploadDocumentModel(models.Model):
  upload_file=models.AutoField(primary_key=True)
  upload_file_name=models.CharField(max_length=100)
  uploaded_video_file=models.FileField(upload_to='uploads/',null=True)
  file_uploaded_at=models.DateTimeField(auto_now=True)
  upload_message=models.CharField(max_length=1000,null=True)
  video_uploader=models.ForeignKey(ClientModel,on_delete=models.CASCADE,null=True,related_name="client_details")
  upload_file_status=models.CharField(max_length=300,help_text='file_status',default='pending')
  upload_file_transfer_status=models.CharField(max_length=300,help_text='file_transfer_status',default='pending')
  
  class Meta:
    db_table='uploaded_files_details'

class PrivateDocument(models.Model):
  upload_file = models.AutoField(primary_key=True)
  file_uploaded_at = models.DateTimeField(auto_now_add=True)
  upload_file_name=models.CharField(max_length=100,null=True)
  uploaded_video_file = models.FileField(storage=PrivateMediaStorage())
  video_uploader = models.ForeignKey(ClientModel,on_delete=models.CASCADE,null=True,related_name='documents')
  upload_message = models.CharField(max_length=1000,null=True)
  upload_file_status=models.CharField(max_length=300,help_text='private_file_status',default='pending')
  upload_file_transfer_status=models.CharField(max_length=300,help_text='private_file_transfer_status',default='pending')
  transfer_status=models.CharField(max_length=300,help_text='transfer_status',default='not-transfer')

  s3_files=models.FloatField(null=True)
  efs_file=models.FloatField(null=True)
  file_count=models.IntegerField(help_text='count',null=True)
  random_id=models.CharField(help_text='random_id',max_length=100,null=True,default='none')
  class Meta:
    db_table='apikey_uploaded_file_details'

# class Document(models.Model):
#   uploaddocument=models.AutoField(primary_key=True)
#   file_name=models.CharField(max_length=100,null=True)
#   uploaded_at = models.DateTimeField(auto_now_add=True)
#   upload = models.FileField()
#   message=models.TextField(null=True)
#   uploaded_by=models.ForeignKey(ClientModel,on_delete=models.CASCADE,null=True,related_name="user_complete_details")
#   class Meta:
#     db_table='upload_document_details'
