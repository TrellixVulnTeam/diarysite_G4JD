from django import forms
from .models import Blog

class BlogForm(forms.ModelForm): 
    class Meta:
        model = Blog #model은 Post를 기반으로
        fields = ['title', 'description'] #타이틀과 바디 생성
