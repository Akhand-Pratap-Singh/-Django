from django.db import models


class student2(models.Model):
	name = models.CharField(max_length=50)
	emailid = models.EmailField(max_length=50)
	contact_no = models.CharField(max_length=12)
	dat = models.DateTimeField()

	def __str__(self):
		return self.name