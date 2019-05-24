from django.contrib import admin
from django.urls import path

from User_App import views
admin.autodiscover()
urlpatterns = [
    path('fileUpload/',views.fileUpload),
    path('addUser/',views.addUser),
    path('getUser/',views.getUsers),
    path('getUserById/<id>',views.getUserById),
    path('deleteById/<id>',views.deleteById),
    path('deleteAll/',views.deleteAll),
    path('imageShow/<code>',views.imageDisplay)

]
