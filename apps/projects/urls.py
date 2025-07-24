from django.urls import path
from apps.projects.views.project_views import *
from apps.projects.views.project_file_views import ListCreateProjectFileAPIView

urlpatterns = [
    path('', ProjectListCreateAPIView.as_view(), name='project-list-create'),  # api/v1/projects/
    path('<int:pk>/', ProjectDetailUpdateDeleteAPIView.as_view(), name='project-detail-update-delete'), # api/v1/projects/1/
    path('files/', ListCreateProjectFileAPIView.as_view(), name='project-file-list-create'), # api/v1/projects/files
]