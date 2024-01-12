from django.db import models

# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.Title