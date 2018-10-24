from django.db import models
# DATETIME
from datetime import datetime

# IMPORT DJANGO USER MODEL
from django.contrib.auth.models import User

class Contact(models.Model):
  user_id = models.ForeignKey(User, on_delete=models.CASCADE) # this deletes everything for that user
  first_name = models.CharField(max_length=25)
  last_name = models.CharField(max_length=25)
  cell_phone = models.CharField(max_length=25, blank=True)
  home_phone = models.CharField(max_length=25, blank=True)
  work_phone = models.CharField(max_length=25, blank=True)
  email = models.CharField(max_length=50, blank=True)
  address = models.CharField(max_length=100, blank=True)
  city = models.CharField(max_length=50, blank=True)
  state = models.CharField(max_length=50, blank=True)
  zipcode = models.CharField(max_length=50, blank=True)
  date_added = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return f'{self.first_name} {self.last_name}'



