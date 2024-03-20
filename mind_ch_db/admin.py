from django.contrib import admin
from .models import User
from .models import PostInfo
from .models import Comment
from .models import Good
from .models import Genre
from .models import Profile
from .models import Memo

# Register your models here.

admin.site.register(User)
admin.site.register(PostInfo)
admin.site.register(Comment)
admin.site.register(Good)
admin.site.register(Genre)
admin.site.register(Profile)
admin.site.register(Memo)