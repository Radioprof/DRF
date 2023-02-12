import graphene
from graphene_django import DjangoObjectType
from users.models import UserModel
from ToDo.models import Project, ToDo


class UserType(DjangoObjectType):
    class Meta:
        model = UserModel
        fields = '__all__'

class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'

class TodoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_todo = graphene.List(TodoType)

    user_by_id = graphene.Field(UserType, id=graphene.String(required=True))
    # project_by_name = graphene.Field(ProjectType, name=graphene.String(required=False))
    # todo_by_project = graphene.List(TodoType, project=graphene.Int(required=False))

    def resolve_all_users(root, info):
        return UserModel.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todo(root, info):
        return ToDo.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return UserType.objects.get(id=id)

        except UserType.DoesNotExist:
            return None

    # def resolve_project_by_name(self, info, name):
    #     try:
    #         return ProjectType.objects.get(name=name)
    #
    #     except ProjectType.DoesNotExist:
    #         return None
    #
    # def resolve_todo_by_project(self, info, project):
    #     try:
    #         return TodoType.objects.get(project=project)
    #
    #     except TodoType.DoesNotExist:
    #         return None


schema = graphene.Schema(query=Query)