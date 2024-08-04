from rest_framework import serializers
from common.utils import get_model_fields
from project_manager.projects_model import ProjectManager

class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectManager
        fields = '__all__'
        