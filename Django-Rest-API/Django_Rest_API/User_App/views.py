
import random
import string

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def fileUpload(request):
         files = request.FILES['file']
         fs = FileSystemStorage()
         photo_code = randomword(20)
         # logger.info('from addTeacher()')
         fs.save(photo_code + '.jpg', files)
         return HttpResponse('ok ok')

def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
