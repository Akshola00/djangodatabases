from django.db import models

# Create your models here.
class Member(models.Model):
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    passwd = models.CharField(max_length=200)
    age = models.IntegerField()
    # class Meta:

    def __str__(self):
        return self.fname +  " " + self.lname