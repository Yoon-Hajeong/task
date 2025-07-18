
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        created_at = serializers.IntegerFied(read_only=True)

    #모르겠어요ㅜ.ㅜ is_overdue 메서드 필드를 추가하여 만기일 경과 여부를 응답에 포함시켜주세요.

        model = Task
        fields = ['title', 'description', 'completed', 'due_date', 'created_at']
