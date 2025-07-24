from rest_framework import serializers # Импортируем serializers из DRF

from apps.projects.models import Project
from apps.tasks.models.tag import Tag # Импортируем нашу модель Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag # Указываем, с какой моделью работает этот сериализатор
        fields = '__all__' # Указываем, что сериализатор должен включать все поля модели


class ProjectShortInfoSerializer(serializers.ModelSerializer):
    """
    Краткий сериализатор для отображения информации о проекте.
    Используется как вложенный сериализатор.
    """
    class Meta:
        model = Project
        fields = ('id', 'name')
