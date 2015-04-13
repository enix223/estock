from django.db import models

class Job(models.Model):
	job_name = models.CharField('Job name', max_length=100)
	batch    = models.CharField('Batch ID', max_length=50)
	start    = models.DateTimeField('Job start time')
	end      = models.DateTimeField('Job end time')
	status   = models.CharField('Job status', max_length=10)
	pid      = models.IntegerField('Job PID')	

class NewStockRate(models.Model):
	plate      = models.CharField('Plate', max_length=3)
	stock_code = models.CharField('Stock code', max_length=6)
	apply_code = models.CharField('Apply code', max_length=6)
	stock_name = models.CharField('Stock Name', max_length=20)
	price      = models.DecimalField('Price', max_digits=7, decimal_places=2)
	apply_date = models.CharField('Aplly date', max_length=10)
	odd_success_rate = models.FloatField('Rate')
