from django import forms
from .models import Comment


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
        widgets = {
            'name': forms.TextInput(attrs={
                'id': 'name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'id': 'email',
                'required': True
            }),
            'body': forms.Textarea(attrs={
                'id': 'body',
                'required': True
            })
        }


class SearchForm(forms.Form):
    query = forms.CharField()
