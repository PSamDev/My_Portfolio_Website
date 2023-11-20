from django.db import models

# Create your models here.
class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.CharField(max_length=20)
    message = models.TextField()
    
    class Meta:
        verbose_name = "Message"        
        verbose_name_plural = "Messages"
        
    def __str__(self):
        return self.name