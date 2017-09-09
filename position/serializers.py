from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('job_name','job_desc','requirement','company','due_date','url')