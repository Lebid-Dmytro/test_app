from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse


class Photo(models.Model):
    image = models.ImageField(blank=True)
    description = models.TextField(max_length=1000, blank=True)

    def get_comment(self):
        return self.comments_set.filter(parent__isnull=True)

    def __str__(self):
        return f"Photo: {self.id}"


class Comments(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    photo_comments = models.ImageField(blank=True, upload_to='images/', validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'gif'])])
    file_comments = models.FileField(blank=True)

    def __str__(self):
        return f"Photo: {self.name}"



