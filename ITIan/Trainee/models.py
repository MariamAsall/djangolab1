from django.db import models
from Course.models import Course  # This imports the Course model we just made

class Trainee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to='trainees/images/', null=True, blank=True) 
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='trainees')

    is_deleted = models.BooleanField(default=False) 

    def __str__(self):
        return f"{self.first_name} {self.last_name}"