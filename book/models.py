from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from markdownx.models import MarkdownxField
# Create your models here.
# Create your models here.

class cart(models.Model):
	user = models.ForeignKey(User)
	payment_type= MarkdownxField()
	payment_id = models.CharField(max_length=10)
	order_date=models.DateTimeField(default=datetime.now())


class products(models.Model):
	product_name= MarkdownxField()
	price = models.IntegerField()
	
	












