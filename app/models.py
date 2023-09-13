from django.db import models

# Create your models here.
class Topic(models.Model):
    TopicName=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.TopicName
    
class Webpage(models.Model):
    TopicName=models.ForeignKey(Topic,on_delete=models.CASCADE)
    Name=models.CharField(max_length=100)
    Email=models.EmailField()
    Date=models.DateField()

    def __str__(self):
        return self.Name