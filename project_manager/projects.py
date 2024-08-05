from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from common import constants as ct
from common.utils import generate_id, get_latest_id
from project_manager.projects_model import ProjectManager
from project_manager.projects_serializer import ProjectManagerSerializer

# Create Project
@api_view(['POST'])
def create_project(request):
    project_details = request.data
    project_details['user'] = request.user_id
    try:
        project_name = project_details.get('project_name')
        if ProjectManager.objects.filter(project_name=project_name, user_id=project_details['user']).exists():
            return JsonResponse(
                {'error': ct.PROJECT_ALREADY_EXISTS},
                status=status.HTTP_400_BAD_REQUEST
            )
        latest_project = get_latest_id(ProjectManager, ct.PROJECT_ID_FULL)
        project_details[ct.PROJECT_ID_FULL] = generate_id(ct.PROJECT_ID, latest_project)
        print(project_details)
        serializer = ProjectManagerSerializer(data=project_details)
        if serializer.is_valid():  
            serializer.save()
            return JsonResponse({'message': ct.PROJECT_CREATED_SUCCESSFULLY}, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
    
# Get Project details
@api_view(['GET'])
def get_project_details(request):
    project_id = request.query_params.get(ct.PROJECT_ID_FULL)
    if not project_id:
        return JsonResponse({'error': ct.PROJECT_ID_REQUIRED}, status=status.HTTP_400_BAD_REQUEST)
    try:
        project_details = ProjectManager.objects.get(project_id=project_id)
        serializer = ProjectManagerSerializer(project_details)
        return JsonResponse({'data': serializer.data}, status=status.HTTP_200_OK)
    except ProjectManager.DoesNotExist:
        return JsonResponse({'error': ct.PROJECT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    except Exception as error:
        return JsonResponse({'error': str(error)}, status=status.HTTP_400_BAD_REQUEST)
    
# Update Project details
@api_view(['PUT'])
def update_project_details(request):
    project_id = request.data.get(ct.PROJECT_ID_FULL)
    if not project_id:
        return JsonResponse({'error': ct.PROJECT_ID_REQUIRED}, status=status.HTTP_400_BAD_REQUEST)
    try:
        project_details = ProjectManager.objects.get(project_id=project_id)
        serializer = ProjectManagerSerializer(project_details, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': ct.PROJECT_UPDATED_SUCCESSFULLY}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except ProjectManager.DoesNotExist:
        return JsonResponse({'error': ct.PROJECT_NOT_FOUND}, status=status.HTTP_404_NOT_FOUND)
    
   