from rest_framework import serializers

from .models import Todo
from django.contrib.auth import get_user_model

User = get_user_model()


class TodoSerializers(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField()

    class Meta:
        model = Todo
        fields = ['title', 'user', 'status', 'absolute_url']
        read_only_fields = ('user',)

    def get_absolute_url(self, obj):
        request = self.context.get('request')
        return request.build_absolute_uri(str(obj).lower().replace(" ", "-"))

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        if request.parser_context.get('kwargs').get('slug'):
            rep.pop('absolute_url')

        return rep


    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['user'] = User.objects.filter(id=request.user.id).first()
        return super().create(validated_data)

