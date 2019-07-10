from rest_framework import serializers
from .models import cpu 
from .models import mem
from .models import disk



class SongsSerializer(serializers.ModelSerializer):
    class Meta:
        model = cpu
        fields = '__all__'

class SongsSerializer2(serializers.ModelSerializer):
    class Meta:
        model = mem
        fields = '__all__'

class SongsSerializer3(serializers.ModelSerializer):
    class Meta:
        model = disk
        fields = '__all__'
        
