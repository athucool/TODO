from django.db import models
from django.urls import reverse
# Create your models here.

class Task(models.Model):
    enter_task=models.CharField(("Enter_task"), max_length=150)

    
    def get_absolute_url(self,pk):
        print("self.id",pk)
        
    def __str__(self):
        return self.enter_task
    

        return reverse("model_detail", kwargs={"pk": self.pk})
    