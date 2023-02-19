from django.contrib import admin
from django.utils.safestring import mark_safe

from spa_app.models import Reviews, Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    pass

