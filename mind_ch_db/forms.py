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

#ログイン
class LoginForm(forms.Form):
    username = forms.CharField(label='名前', max_length=150)
    password = forms.CharField(label='パスワード', widget=forms.PasswordInput())
   
   

class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        fields = ['title', 'content']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # ビューから渡されたユーザーオブジェクトを取得
        super(MemoForm, self).__init__(*args, **kwargs)
        self.user = user  # ユーザーオブジェクトをインスタンス変数に保存

    def save(self, commit=True):
        memo = super().save(commit=False)  # コミットを保留したメモオブジェクトを取得
        if self.user:
            memo.user_id = self.user  # ユーザーをメモの user_id に設定
        if commit:
            memo.save()  # メモを保存
        return memo


class PostInfoForm(forms.ModelForm):
    class Meta:
        model = PostInfo
        fields = ['genre_id', 'post_title', 'post_content']
        widgets = {
            'post_title': forms.TextInput(attrs={'placeholder': '名前'})
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)  # ビューから渡されたユーザーオブジェクトを取得
        super(PostInfoForm, self).__init__(*args, **kwargs)
        self.user = user  # ユーザーオブジェクトをインスタンス変数に保存

    def save(self, commit=True):
        post = super().save(commit=False)  # コミットを保留した投稿オブジェクトを取得
        if self.user:
            post.user_id = self.user  # ユーザーを投稿の user_id に設定
        if commit:
            post.save()  # 投稿を保存
        return post


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