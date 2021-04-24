from django.db import models

# Create your models here.
class Team(models.Model):
    collegename = models.CharField(max_length=255)
    teamname = models.CharField(max_length=255)
    name1 = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50)
    name3 = models.CharField(max_length=50)
    email1 = models.EmailField(max_length=100)
    email2 = models.EmailField(max_length=100)
    email3 = models.EmailField(max_length=100)
    phnumber1 = models.CharField(max_length=50)
    phnumber2 = models.CharField(max_length=50)
    phnumber3 = models.CharField(max_length=50)
    proof_pic=models.FileField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.collegename
    