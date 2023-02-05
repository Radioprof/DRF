from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from .models import ToDo, Project
from .serializers import TodoSerializer, ProjectSerializer
from .filters import TodoFilter, ProjectFilter


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20

class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10

class TodoViewSet(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = TodoSerializer
    pagination_class = TodoLimitOffsetPagination
    # filterset_class = TodoFilter

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    pagination_class = ProjectLimitOffsetPagination
    # filterset_class = ProjectFilter
