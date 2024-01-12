from django.db import models

# Create your models here.
class Comments(models.Model):
    post_id = models.IntegerField()
    comment = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.post_id} {self.comment}"
    
    