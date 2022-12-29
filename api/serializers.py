from rest_framework.serializers import ModelSerializer
from .models import TestModel

class TestModelSerializer(ModelSerializer):
    class Meta:
        model = TestModel
        fields = ['title','desc']

class TestModelGetSerializer(ModelSerializer):
    class Meta:
        model = TestModel
        fields = ['id','title','desc']
