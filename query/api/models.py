from django.db import models


# Create your models here.
class QueryPost(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class QueryComment(models.Model):
    post = models.ForeignKey(
        QueryPost, related_name="comments", on_delete=models.CASCADE
    )

    comment = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.post_id} - {self.comment}"
