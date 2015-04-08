from django.db import models

class Job(models.Model):
	job_name = models.CharField('Job name', max_length=100)
	batch    = models.CharField('Batch ID', max_length=50)
	start    = models.DateTimeField('Job start time')
	end      = models.DateTimeField('Job end time')
	status   = models.CharField('Job status', max_length=10)
	pid      = models.IntegerField('Job PID')	
