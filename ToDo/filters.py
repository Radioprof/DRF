from django_filters import rest_framework as filters
from .models import ToDo, Project


class TodoFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='Project.name')

    class Meta:
        model = ToDo
        fields = ['name']

class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']