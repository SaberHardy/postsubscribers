from django import forms

from blog.models import Post, Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'rows': 4,
    }))

    class Meta:
        model = Post
        fields = ['title', 'content']


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',
                                      widget=forms.TextInput(
                                          attrs={
                                              'placeholder': 'Add your comment here ...',
                                              'class': 'mt-3'
                                          }))

    class Meta:
        model = Comment
        fields = ('content',)
