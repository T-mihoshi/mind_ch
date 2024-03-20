from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True, null=True)
    picture = models.FileField(upload_to='user/', blank=True, null=True)

    def __str__(self):
        return self.user.username
    

class Good(models.Model):
    post_info_id = models.ForeignKey(
        'postinfo', on_delete=models.CASCADE)
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE)
    creat_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)


#ここからテーブル定義
class User(models.Model):
    user_name = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

#投稿
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(default=timezone.datetime.now)

class PostInfo(models.Model):
    genre_id = models.ForeignKey(
        'genre', on_delete=models.SET_NULL,null=True)
    post_title = models.CharField(max_length=50)
    post_content = models.TextField(max_length=1000)
    reaction_count = models.IntegerField(null=True, blank=True)
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)


class Comment(models.Model):
    Post_info_id = models.ForeignKey(
        'postinfo', on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    reaction_count = models.IntegerField()
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

class Genre(models.Model):
    genre_name = models.CharField(max_length=30)
    creat_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)
    
    def __str__(self):
        return self.genre_name

class Memo(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    create_at = models.DateTimeField(default=timezone.datetime.now)
    update_at = models.DateTimeField(default=timezone.datetime.now)

    def __str__(self):
        return self.title



"""genre_id = models.ForeignKey(
      'genre', on_delete=models.SET_NULL,null=True)"""


"""
class Person(models.Model):
    Fiast_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)

"""