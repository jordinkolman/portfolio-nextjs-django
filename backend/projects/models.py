from django.db import models

class Project(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='images/')
    url = models.URLField()
    github = models.URLField()
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
