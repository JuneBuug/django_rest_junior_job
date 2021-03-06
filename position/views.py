import django_filters.rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination
from rest_framework import viewsets, mixins, generics
from rest_framework.generics import GenericAPIView
from rest_framework import filters
from .models import Job
from .serializers import JobSerializer
# Create your views here.


# class job_api(GenericAPIView, mixins.ListModelMixin):
#     queryset = Job.objects.all()
#     serializer_class = JobSerializer
#
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
#
#     def get_queryset(self):
#         queryset = Job.objects.all()
#         return queryset
#

# query params 로 필터링 하는 경우
# class job_api(GenericAPIView, mixins.ListModelMixin):
#     serializer_class = JobSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def get_queryset(self):
#         queryset = Job.objects.all()
#         company_name = self.request.query_params.get('company', None)
#         if company_name is not None:
#             queryset = queryset.filter(company__contains=company_name)
#         return queryset


# class job_api(generics.ListAPIView):
#     serializer_class = JobSerializer
#     queryset = Job.objects.all()
#     filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
#     filter_fields = ('job_name', 'company')
#

class JunePagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page'
    max_page_size = 1000


class job_api(generics.ListAPIView):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    filter_backends = (filters.SearchFilter,django_filters.rest_framework.DjangoFilterBackend,filters.OrderingFilter,)
    search_fields = ('job_name', 'company')
    filter_fields = ('job_name', 'company')
    ordering_fields = ('job_name','company')
    ordering = ('job_name')


class job_url_api(GenericAPIView, mixins.ListModelMixin):

    serializer_class = JobSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)

    def get_queryset(self):
        company_name = self.kwargs['company']
        job = self.kwargs['job_name']
        return Job.objects.filter(company__contains=company_name).filter(job_name__contains=job)


