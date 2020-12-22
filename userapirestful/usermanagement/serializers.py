from rest_framework import serializers
from .models import Usertable

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Usertable
        fields = ['email', 'username', 'password'] 
		