from django import forms


from .models import Comments


class CommentForm(forms.ModelForm):
    # captcha = ReCaptchaField()

    class Meta:
        model = Comments
        fields = ('name', 'email', 'text', 'photo_comments', 'file_comments',)
        # widgets = {
        #     'name': forms.TextInput(attrs={"class": "form-control border"}),
        #     'email': forms.EmailInput(attrs={"class": "form-control border"}),
        #     'text': forms.Textarea(attrs={"class": "form-control border"}),
        #     'photo_comments': forms.ImageField(attrs={"class": "form-control border"}),
        #     'file_comments': forms.FileField(attrs={"class": "form-control border"})
        # }