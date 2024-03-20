from django.contrib import admin
from django.urls import path
from . import views
from django.urls import path, include
from .views import index, post_info_detail, good_list

from django.contrib.auth import views as auth_views


#他のページの場合、index→○○○○ (ログイン画面ならloginになる。)
#path('admin/', admin.site.urls),
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base', views.base, name='base'),
    path('comment', views.comment, name='comment'),
    path('good_list', views.good_list, name='good_list'),
    path('id_pass', views.id_pass, name='id_pass'),
    path('', views.index, name='index'),
    path('my_posts', views.my_posts, name='my_posts'),
    path('password_modifying', views.password_modifying, name='password_modifying'),
    path('post', views.create_post, name='create_post'),
    path('posts_edit', views.posts_edit, name='posts_edit'),
    path('profile', views.profile, name='profile'),
    path('registration', views.registration, name='registration'),
    path('register', views.register, name='register'),
    path('user_login', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('info', views.info, name='info'),
    path('', index, name='index'),
    path('post-info/<int:post_info_id>/', post_info_detail, name='post_info_detail'),




    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('', include('django.contrib.auth.urls')),
    path('good_toggle/<int:post_info_id>/', views.good_toggle, name='good_toggle'),

    path('memo_list', views.memo_list, name='memo_list'),
    path('memo/<int:memo_id>/', views.memo_detail, name='memo_detail'),
    path('memo/new/', views.memo_create, name='memo_create'),
    path('memo/<int:memo_id>/edit/', views.memo_edit, name='memo_edit'),
    path('memo/<int:memo_id>/delete/', views.memo_delete, name='memo_delete'),
    path('genre_list/<int:genre_id>/', views.genre_list, name='genre_list'),
    path('post_list', views.post_list, name='post_list'),
path('posts/<int:post_id>/edit/', views.posts_edit, name='posts_edit'),

]


