from rest_framework import generics
from .models import cpu
from .models import mem
from .models import disk
from .serializers import SongsSerializer
from .serializers import SongsSerializer2
from .serializers import SongsSerializer3
from rest_framework.views import APIView, Response
import psutil
import shutil
import subprocess
import os

class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = cpu.objects.all()
    serializer_class = SongsSerializer
    

class ListSongsView2(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = mem.objects.all()
    serializer_class = SongsSerializer2
    
class ListSongsView3(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = disk.objects.all()
    serializer_class = SongsSerializer3

#class currentsView(APIView):
#
#    total, used, free = shutil.disk_usage("/")
#    def get(self, request, format=None):
#        obj_Disk = psutil.disk_usage('/')
#        used = obj_Disk.used / (1024.0 ** 3)
#        strings ={
#        "CPU " : psutil.cpu_percent(),
#        "Memory used" : psutil.virtual_memory()[3],
#        "Disk Used" : used
#        }
#        return Response(str(strings))
#        #return "{} - {}".format(self.avgused, self.avgaval)

class currentsView(APIView):

    #total, used, free = shutil.disk_usage("/")
    def get(self, request, format=None):
  
        obj_Disk = psutil.disk_usage('/')
        used = obj_Disk.used / (1024.0 ** 3)
      
        strings ={
        "CPU usage": "{0:.2f}".format(100.0-float(os.popen("(mpstat | head -4 | tail -1 | awk '{print $13}')").read())),
        "Memory used": "{0:.5f}".format(int(os.popen("(free | head -2 | tail -1 | awk '{print $3}')").read()) /(1024.0 ** 3)), 
        "Disk used": "{0:.5f}".format(int(os.popen("(df --total | tail -n 1 | awk '{print $3}')").read()) /(1024.0 ** 3))
       
        }
        
        return Response(str(strings))
        


   
    

    


