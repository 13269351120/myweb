from django.db import models

# Create your models here.


from django.utils import timezone

class Dailyjobs(models.Model):
	
	testname = models.CharField(max_length=50)
	
	parameters = models.CharField(max_length=50)
	
	pub_date = models.DateTimeField(default=timezone.now , editable = False)
	user = models.CharField(max_length = 20)
	state = models.IntegerField(default=0 , editable = False )  
	
	mean_error = models.FloatField(default = -1.0,editable = False)  
	medium_error = models.FloatField(default = -1.0,editable = False)
	time_cost = models.FloatField(default = -1.0 ,editable = False)
	
	class Meta:
		ordering = ('-pub_date',)
		
	
	def __unicode__(self):
		return self.testname  
		