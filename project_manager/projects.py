import json
from django.http import JsonResponse
from rest_framework import status
from common.utils import apply_filters, apply_search_sort_filter_pagination, custom_sort, get_paginated_data, get_search_results
from project_manager.projects_model import ProjectManager
from project_manager.projects_serializer import ProjectManagerSerializer
from rest_framework.decorators import api_view
from django.db.models import Count, Q
from common import constants as ct

def get_project_db_data(user_id):
    project_details = ProjectManager.objects.filter(user=user_id)
    return project_details

@api_view(['GET'])
def get_project_cards_data(request):
    user_id = request.user_id
    try:
        project_details = get_project_db_data(user_id)
        count = project_details.aggregate(
            planning=Count(ct.PROJECT_ID, filter=Q(project_status=ct.PLANNING)),
            in_progress=Count(ct.PROJECT_ID, filter=Q(project_status=ct.IN_PROGRESS)),
            completed=Count(ct.PROJECT_ID, filter=Q(project_status=ct.COMPLETED)),
            closed=Count(ct.PROJECT_ID, filter=Q(project_status=ct.CLOSED)),
            personal=Count(ct.PROJECT_ID, filter=Q(project_status=ct.PERSONAL)),
            organization=Count(ct.PROJECT_ID, filter=Q(project_status=ct.ORGANIZATION))
        )
        return JsonResponse({'data': count, }, status=status.HTTP_200_OK)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def get_projects_table_data(request):
    page = request.query_params.get('page', '1')
    limit = request.query_params.get('limit', '10')
    search_input = request.query_params.get('search_input', '')
    sort_param = request.query_params.get('sort', 'created_at desc')
    filters = request.query_params.get('filters', '{}')
    filters = json.loads(filters)
    user_id = request.user_id
    total_count = 0
    try:
        project_details = get_project_db_data(user_id)
        project_details = ProjectManagerSerializer(project_details, many=True).data
        total_count = len(project_details)
        result = apply_search_sort_filter_pagination(project_details, filters,search_input,sort_param,page,limit)
        response_data = {
            'project_list': result,
            'total_count': total_count,
        }
        return JsonResponse({'data': response_data, }, status=status.HTTP_200_OK)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
