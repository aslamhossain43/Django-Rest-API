from django.contrib import admin
from django.urls import path

from User_App import views
admin.autodiscover()
urlpatterns = [
    path('fileUpload/',views.fileUpload,name='fileUPload'),

]
