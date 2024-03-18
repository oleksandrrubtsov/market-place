from django.db import models

# Create your models here.

class Author(models.Model):
    # Fields for the Author model
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(blank=True, null=True)

    
    def __str__(self) -> str:
        return self.first_name  + " " + self.last_name