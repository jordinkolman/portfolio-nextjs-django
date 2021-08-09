from django.shortcuts import render
from .serializers import ProjectSerializer
from rest_framework import viewsets
from .models import Project

class ProjectView(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()