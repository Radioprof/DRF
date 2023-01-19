from rest_framework.viewsets import ModelViewSet
from rest_framework import mixins, viewsets
from rest_framework.pagination import LimitOffsetPagination
from .models import UserModel
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer


class UserCustomViewSet(mixins.UpdateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

