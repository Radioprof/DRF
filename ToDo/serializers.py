from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ToDo, Project


class ProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TodoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
