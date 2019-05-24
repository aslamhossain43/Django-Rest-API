import datetime
import os
import random
import string

from PIL import Image
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from User_App.models import User
from User_App.serializers import UserSerializer


def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
code = ''
@csrf_exempt
def fileUpload(request):
         global code
         code = randomword(20)
         files = request.FILES['file']
         fs = FileSystemStorage()
         fs.save(code+'.jpg', files)
         return HttpResponse('ok ok')

@csrf_exempt
def getUsers(request):
          users = User.objects.all()
          serialized_user = UserSerializer(users, many=True)
          return JsonResponse(serialized_user.data,safe=False)
@csrf_exempt
def getUserById(request,id):
          user = User.objects.get(id = id)
          serialized_user = UserSerializer(user)
          return JsonResponse(serialized_user.data,safe=False)
@csrf_exempt
def addUser(request):
         user = JSONParser().parse(request)
         serialized_user = UserSerializer(data=user)
         if serialized_user.is_valid():
            serialized_user.save(user_date = datetime.datetime.now(),user_photo = code)
            return JsonResponse(serialized_user.data,status=status.HTTP_201_CREATED)
         return JsonResponse(serialized_user.data,status=status.HTTP_400_BAD_REQUEST)
@csrf_exempt
def deleteById(request,id):
    user = User.objects.get(id = id)
    os.remove('images/'+user.user_photo+'.jpg')
    user.delete()
    return HttpResponse('delete by id')
@csrf_exempt
def deleteAll(request):
    users = User.objects.all()
    for user in users:
     os.remove('images/'+user.user_photo+'.jpg')
    users.delete()
    return HttpResponse('deleted all users')

@csrf_exempt
def imageDisplay(request,code):
    image_data = open('images/'+code+'.jpg', 'rb').read()
    return HttpResponse(image_data, content_type="image/jpg")

