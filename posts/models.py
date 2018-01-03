from django.db import models
from django.core.urlresolvers import reverse


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=20)
	image = models.ImageField(null=True, blank=True,
			width_field="width_field",
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	# auto_now=True means every single time its saved in the database this will be saved 
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	# auto_now=True means whenever its added to the database then its saved onetime
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		# return "/posts/%s" %(self.id)
		# the above is hardcoding. The following is a better way
		return reverse('detail', kwargs={'id':self.id})

	def delete_post(self):
		pass
		
	class Meta:
		ordering = ['-timestamp', '-updated']	

