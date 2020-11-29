from django import forms
from . models import  *

class ProjectUpload(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','image','description','link')
