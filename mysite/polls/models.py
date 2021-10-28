from django.db import models

# Create your models here.
class Name(models.Model):
    student_name = models.CharField(max_length=200)

    def __str__(self):
        return self.student_name

        