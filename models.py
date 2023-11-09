from django.db import models

# Create your models here.
class team(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField( upload_to='teams' )
    para = models.TextField(max_length=250)
    def __str__(self) :
        return self.title
class book(models.Model):
    F_name = models.CharField(max_length=50)
    S_name= models.CharField(max_length=50)
    phone = models.IntegerField()
    team1 = models.CharField(max_length=50)
    team2 = models.CharField(max_length=50)
    date = models.CharField(max_length=50)
     