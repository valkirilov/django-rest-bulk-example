from api.models import Teacher
from rest_framework import serializers

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'degree', 'short', 'email', 'department',)
        depth = 2