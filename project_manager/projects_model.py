from django.db import models
from common.utils import get_model_fields
from common import constants as ct

class ProjectManager(models.Model):
    project_id = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT, primary_key=True)
    project_name = models.CharField(max_length=ct.CHAR_MEDIUM_LIMIT)
    project_description = models.CharField(max_length=ct.CHAR_VERY_LONG_LIMIT)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    project_type = models.CharField(
        max_length=ct.CHAR_MEDIUM_LIMIT,
        choices=ct.PROJECT_TYPE_CHOICES,
    )
    project_status = models.CharField(
        max_length=ct.CHAR_MEDIUM_LIMIT,
        choices=ct.PROJECT_STATUS,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "project_manager"