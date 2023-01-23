from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project

class ProjectSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
