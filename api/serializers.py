from rest_framework import serializers
from api.models import Todo

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'