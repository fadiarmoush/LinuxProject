from django.db import models
import shutil


class cpu(models.Model):
    # song title
    avg = models.FloatField(primary_key=True)
    # name of artist or group/band
    #artist = models.CharField(max_length=255, null=False)
#
#    def __str__(self):
#        return "{} - {}".format(self.title, self.artist)

    def __str__(self):
        return self.avg
    class Meta:
        db_table='cpuInfo'


class mem(models.Model):
    # song title
    avgused = models.FloatField(primary_key=True)
    avgaval = models.FloatField(primary_key=True)
    # name of artist or group/band
    #artist = models.CharField(max_length=255, null=False)
#
#    def __str__(self):
#        return "{} - {}".format(self.title, self.artist)

    def __str__(self):
         return "{} - {}".format(self.avgused, self.avgaval)
    class Meta:
        db_table='memInfo'

class disk(models.Model):
    # song title
    avgused = models.FloatField(primary_key=True)
    avgaval = models.FloatField(primary_key=True)
    # name of artist or group/band
    #artist = models.CharField(max_length=255, null=False)
#
#    def __str__(self):
#        return "{} - {}".format(self.title, self.artist)

    def __str__(self):
         return "{} - {}".format(self.avgused, self.avgaval)
    class Meta:
        db_table='diskInfo'
#        
#class real(models.Model):
# 
#    total, used, free = shutil.disk_usage("/")
#
#    def __str__(self):
#         return "{} - {}".format(self.used, self.free)
      
         
