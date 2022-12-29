from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UserModel

class UserModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
