from django.urls import path

from . import views


urlpatterns = [
    path('', views.PhotoView.as_view(), name='photo_list'),
    path('<int:pk>/', views.PhotoDescriptionView.as_view()),
    path('review/<int:pk>/', views.AddComments.as_view(), name='add_comments'),

]