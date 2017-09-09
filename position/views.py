from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.generics import GenericAPIView

from .models import Job
from .serializers import JobSerializer
# Create your views here.


class job_api(GenericAPIView, mixins.ListModelMixin):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def get_queryset(self):
        queryset = Job.objects.all()
        return queryset