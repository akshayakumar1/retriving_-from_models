from django.db import models

# Create your models here.

class Topics(models.Model):
    topic_name=models.CharField(max_length=200,primary_key=True)
    def __str__(self):
        return self.topic_name
    
    
class Webpages(models.Model):
    topic_name=models.ForeignKey(Topics,on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    url=models.URLField()
    
    def __str__(self):
        return self.name
    

class Acces_rec(models.Model):
    name=models.ForeignKey(Webpages,on_delete=models.CASCADE)
    date=models.DateField()
    
    
    
        
        
    
