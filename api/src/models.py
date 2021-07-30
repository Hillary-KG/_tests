from django.db import models


# Create your models here.
class Points(models.Model):
    closest_pair = models.CharField(max_length=50, null=False)
    distance = models.CharField(max_length=30, null=False)
    input_str = models.TextField(null=False)

    def __str__(self):
        return f"{self.closest_pair}"

    class Meta:
        ordering = ['input_str']
