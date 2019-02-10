from django.forms import ModelForm
from mysite.models import Post

class PostFrom(ModelForm):
    class Meta:
        model = Post
        fields = ['title','text']