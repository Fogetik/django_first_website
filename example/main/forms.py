from .models import Blog
from django.forms import ModelForm, TextInput, Textarea


class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = ["title", "text_blog"]
        widgets = {
            "title" : TextInput(attrs={
                'class' : 'form-control',
                'placeholder' : 'Название'
            }),
            "text_blog": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'История'
            })
        }
