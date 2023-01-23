from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ToDo

class TodoSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
