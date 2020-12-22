from rest_framework import viewsets
from . import models
from . import serializers

class UserViewsets(viewsets.ModelViewSet):
    queryset = models.Usertable.objects.all()
    serializer_class = serializers.Userserializer