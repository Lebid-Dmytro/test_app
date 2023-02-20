from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import DetailView

from spa_app.forms import CommentForm
from spa_app.models import Photo
from test import settings


class PhotoView(View):
    def get(self, request):
        list_view = Photo.objects.all()
        return render(request, 'index.html', {'list_view': list_view})


class PhotoDescriptionView(View):
    def get(self, request, pk):
        about = Photo.objects.get(id=pk)
        return render(request, 'detail.html', {'about': about, })


class AddComments(View):
    '''Відгуки'''
    def post(self, request, pk):
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get('parent', None):
                form.parent_id = int(request.POST.get('parent'))
            form.photo_id = pk
            form.save()
        return redirect(f'/{pk}')


