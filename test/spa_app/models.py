from django.db import models
from django.urls import reverse


class Photo(models.Model):
    image = models.ImageField(blank=True)
    description = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return f"Photo: {self.id}"


class Reviews(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    text = models.TextField(max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    image_reviews = models.ImageField()
    file_reviews = models.FileField()

    def __str__(self):
        return f"{self.name} - {self.image}"


