from typing import Any
from django import forms
from django.contrib.auth.models import User
from mind_ch_db.models import Profile
from .models import Memo
from .models import PostInfo
from .models import Comment



class UserForm(forms.ModelForm):
    email = forms.EmailField(label='メールアドレス', required=False)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
    
    class Meta():
        model = User
        fields = ('username', 'email', 'password')

class ProfileForm(forms.ModelForm):
    website = forms.URLField(label='ホームページ')
    picture = forms.FileField(label='写真')
    
    class Meta():
        model = Profile
        fields = ('website', 'picture')

class LoginForm(forms.Form):
    username = forms.CharField(label='名前', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
   
   
class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content']
   

class PostInfoForm(forms.ModelForm):
    

    class Meta:
        model = PostInfo
        fields = ['genre_id', 'post_title', 'post_content']
        widgets = {
            'post_title': forms.TextInput(attrs={'placeholder': '名前'})
        }
    

#投稿編集
class PostInfoForm(forms.ModelForm):
    class Meta:
        model = PostInfo
        fields = ['genre_id', 'post_title', 'post_content']  # 編集可能なフィールドを指定します


#投稿に対してコメントする
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
    
    
    """
    confirm_password = forms.CharField(label='パスワード再入力', widget=forms.PasswordInput())

    def clean(self):
        cleaned_date = super().clean()
        password = cleaned_date['password']
        confirm_password = cleaned_date['confirm_password']
        if password !=confirm_password:
            raise forms.ValidationError('パスワードが一致していません')
        """