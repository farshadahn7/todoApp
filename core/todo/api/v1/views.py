from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from ...serializers import TodoSerializers
from ...models import Todo



class TodoListView(viewsets.ModelViewSet):
    serializer_class = TodoSerializers
    permission_classes = [IsAuthenticated]
    lookup_field = 'slug'
    def get_queryset(self):
        return Todo.objects.filter(user__id = self.request.user.id)