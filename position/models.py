from django.db import models

# Create your models here.


class Job(models.Model):
    job_name = models.CharField(max_length=128)
    job_desc = models.TextField()
    requirement = models.TextField()
    company = models.CharField(max_length=128)
    due_date = models.DateTimeField()
    url = models.CharField(max_length=512)

    def __str__(self):
        return self.job_name + "("+ self.company+")"

