from django.shortcuts import render, redirect
from django.http import HttpResponse
from mind_ch_db.forms import UserForm, ProfileForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Memo, Genre
from .forms import MemoForm
from .forms import PostInfoForm
from .forms import CommentForm


# Create your views here.

def base(request):
    return render(request, 'base.html')
def comment(request):
    return render(request, 'comment.html')
def good_list(request):
    return render(request, 'good_list.html')
def id_pass(request):
    return render(request, 'id_pass.html')
def index(request):
    return render(request, 'index.html')
def my_posts(request):
    return render(request, 'my_posts.html')
def password_modifying(request):
    return render(request, 'password_modifying.html')
def post(request):
    return render(request, 'post.html')
def posts_edit(request):
    return render(request, 'posts_edit.html')
def profile(request):
    return render(request, 'profile.html')
def base(request):
    return render(request, 'base.html')
def base(request):
    return render(request, 'base.html')
def index(request):
    return render(request, 'index.html')
def registration(request):
    return render(request, 'registration.html')
def register(request):from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def register(request):
    error_message = ""

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            login(request, user)  # ユーザーをログインさせる
            return redirect('index')
        else:
            # エラーメッセージの生成
            if 'password1' in user_form.errors:
                error_message = 'パスワードは8文字以上で入力してください。'
            elif 'username' in user_form.errors:
                error_message = '存在するユーザーです。'
            else:
                error_message = '入力が正しくありません。'
    else:
        user_form = UserForm()

    return render(request, 'registration.html', {'user_form': user_form, 'error_message': error_message})


"""return render(request, 'registration.html', context={
    'user_form': user_form,
    'profile_form': profile_form,
    'success_message': '登録が成功しました。',  # 必要に応じて
})"""

"""
def user_login(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse('アカウントがアクティブではありません')
        else:
            return HttpResponse('ユーザーが存在しません')
    return render(request, 'login.html', context={'login_form': login_form})
"""
# views.py

from django.contrib.auth.views import LoginView
from django.urls import reverse

class CustomLoginView(LoginView):
    template_name = 'login.html'  # ログイン画面のテンプレート
    redirect_authenticated_user = True  # ログイン済みのユーザーをリダイレクトするかどうか
    success_url = '/profile/' # ログイン成功時のリダイレクト先

login_view = CustomLoginView.as_view()

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def info(request):
    return HttpResponse('ログインしています')

from .models import PostInfo, Comment

def post_info (request):
    post_infos = PostInfo.objects.filter(id=1).all()
    return render(request, 'comment.html', {'post_infos': post_infos})

from django.shortcuts import render, get_object_or_404

from django.shortcuts import render
from .models import PostInfo, Good

def index(request):
    post_infos = PostInfo.objects.all().order_by('-create_at')
    good_counts = {}
    for post_info in post_infos:
        good_counts[post_info.id] = Good.objects.filter(post_info_id=post_info.id).count()
    return render(request, 'index.html', {'post_infos': post_infos, 'good_counts': good_counts})

#ジャンル表示画面　genre_choice
def genre_choice(request):
    genres_all = Genre.objects.all() # ジャンルタイトル一覧
    return render(request, 'genre_choice.html', {'genres_all': genres_all})

#投稿へのコメント
def post_info_detail(request, post_info_id):
    post_info = get_object_or_404(PostInfo, pk=post_info_id)
    comments = Comment.objects.filter(Post_info_id=post_info_id)
    good_count = Good.objects.filter(post_info_id=post_info_id).count()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.Post_info_id = post_info
            comment.save()
            return redirect('post_info_detail',post_info_id=post_info_id)
    else:
        form = CommentForm()
    return render(request, 'comment.html', {
        'post_info': post_info,
        'comments': comments,
        'form': form,
        'good_count': good_count,
        })


#投稿一覧
def post_list(request):
    posts = PostInfo.objects.all().order_by('-create_at')
    return render(request, 'post_list.html', {'posts': posts})


#投稿を編集
def posts_edit(request, post_id):
    post = get_object_or_404(PostInfo, pk=post_id)
    if request.method == 'POST':
        form = PostInfoForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # 編集後に投稿一覧ページにリダイレクト
    else:
        form = PostInfoForm(instance=post)
    return render(request, 'posts_edit.html', {'form': form})

#いいね☆機能
from .models import Good
def good_toggle(request, post_info_id):
    user = request.user
    post = get_object_or_404(PostInfo, pk=post_info_id)
    good, created = Good.objects.get_or_create(user_id=user, post_info_id=post)
    if not created:
        good.delete()
    return redirect('post_info_detail', post_info_id=post_info_id)

#メモ機能

def memo_list(request):
    memoss = Memo.objects.all().order_by('-create_at')
    return render(request, 'memo_list.html', {'memoss': memoss})

def memo_detail(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    return render(request, 'memo_detail.html', {'memo': memo})

def memo_create(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('memo_list')
    else:
        form = MemoForm()
    return render(request, 'memo_form.html', {'form': form})

def memo_edit(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)

    if request.method == 'POST':
        form = MemoForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            return redirect('memo_detail', memo_id=memo_id)
    else:
        form = MemoForm(instance=memo)
    
    return render(request, 'memo_edit_form.html', {'form': form})

def memo_delete(request, memo_id):
    memo = get_object_or_404(Memo, pk=memo_id)
    memo.delete()
    return redirect('memo_list')


#いいね一覧
def good_list(request):
    user = request.user
    goods = Good.objects.filter(user_id=user).select_related('post_info_id').order_by('-create_at')
    post_info_good = [good.post_info_id for good in goods]
    return render(request, 'good_list.html', {'post_info_good': post_info_good})

#ジャンル別投稿表示
def genre_list(request, genre_id):
    genres = PostInfo.objects.filter(genre_id=genre_id).all().order_by('-create_at')
    return render(request, 'genre_list.html', {'genres': genres})

#投稿する
def create_post(request):
    if request.method == 'POST':
        form = PostInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')  # 投稿一覧ページにリダイレクト
    else:
        form = PostInfoForm()
    return render(request, 'create_post.html', {'form': form})

"""
from .models import Good
@login_required
def good_list(request, post_info_id):# ログインしているユーザーのIDを取得
    post_info = get_object_or_404(PostInfo, pk=post_info_id)#受け取った記事
    good, created = Good.objects.get_or_create(post_info_id=post_info.id, user_id=post_info_id)#createにセーブメソッドが組み込まれている
    if not created: 
        good.delete() # Goodオブジェクトが既に存在する場合は削除
    return redirect(request.META.get('HTTP_REFERER', 'index'))# 元のページにリダイレクト

from django.db.models import Q

def good_list_show(request, post_info_id):
    post_infos = PostInfo.objects.filter(Q(id=post_info_id) & Q(good__post_info_id=post_info_id)).all()  # すべての postInfo レコードを取得
    return render(request, 'good_list.html', {'post_infos': post_infos})
"""