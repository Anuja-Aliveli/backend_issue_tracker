import json
from django.http import JsonResponse
from rest_framework import status
from common.table_column_mappings import PROJECT_COLUMNS_MAPPING, PROJECTS_ACTION_OPTIONS
from common.utils import apply_filters, apply_search_sort_filter_pagination, custom_sort, get_count_data, get_paginated_data, get_search_results
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
        count_db_data = project_details.aggregate(
            planning=Count(ct.PROJECT_ID, filter=Q(project_status=ct.PLANNING)),
            in_progress=Count(ct.PROJECT_ID, filter=Q(project_status=ct.IN_PROGRESS)),
            completed=Count(ct.PROJECT_ID, filter=Q(project_status=ct.COMPLETED)),
            closed=Count(ct.PROJECT_ID, filter=Q(project_status=ct.CLOSED)),
            personal=Count(ct.PROJECT_ID, filter=Q(project_status=ct.PERSONAL)),
            organization=Count(ct.PROJECT_ID, filter=Q(project_status=ct.ORGANIZATION))
        )
        count_data = get_count_data(count_db_data)
        return JsonResponse({ct.DATA: count_data, }, status=status.HTTP_200_OK)
    except Exception as error:
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)
        
def attach_projects_route_link(projects_list):
    result = []
    for index, item in enumerate(projects_list):
        item['rowId'] = index
        item[ct.ROUTE_LINK] = {
            str(ct.PROJECT_ID): f"/projects/view/{item[ct.PROJECT_ID]}",
            'edit_project': f"/projects/edit/{item[ct.PROJECT_ID]}"
        }
        if item[ct.PROJECT_STATUS_TEXT] != ct.CLOSED:
            item[ct.ACTION_OPTIONS] = PROJECTS_ACTION_OPTIONS
        else:
            item[ct.ACTION_OPTIONS] = PROJECTS_ACTION_OPTIONS[:-1]
        result.append(item)
    return result
        
@api_view(['GET'])
def get_projects_table_data(request):
    page = request.query_params.get(ct.PAGE, '1')
    limit = request.query_params.get(ct.LIMIT, '10')
    search_input = request.query_params.get(ct.SEARCH_INPUT, '')
    sort_param = request.query_params.get(ct.SORT, 'created_at desc')
    filters = request.query_params.get(ct.FILTERS, '{}')
    filters = json.loads(filters)
    user_id = request.user_id
    total_count = 0
    try:
        project_details = get_project_db_data(user_id)
        project_details = ProjectManagerSerializer(project_details, many=True).data
        total_count = len(project_details)
        result = apply_search_sort_filter_pagination(project_details, filters,search_input,sort_param,page,limit)
        result = attach_projects_route_link(result)
        column_data = PROJECT_COLUMNS_MAPPING
        response_data = {
            'column_data': column_data,
            'project_list': result,
            'total_count': total_count,
        }
        return JsonResponse({ct.DATA: response_data, }, status=status.HTTP_200_OK)
    except Exception as error:
        return JsonResponse({ct.ERROR: str(error)}, status=status.HTTP_400_BAD_REQUEST)
