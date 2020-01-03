from django.db import models

class Job(models.Model): # Model name is Job
    # it will store Images in images folder
    image = models.ImageField(upload_to='images/')
    # Summary
    summary = models.CharField(max_length=200)
    

