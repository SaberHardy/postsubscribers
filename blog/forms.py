from django import forms

from blog.models import Post


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
    }))

    class Meta:
        model = Post
        fields = ['title', 'content']
