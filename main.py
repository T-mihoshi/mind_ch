import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mind_ch_db.settings')
from django import setup
setup()

from mind_ch_db.models import PostInfo, Genre  #ここはmind_ch_dbの中のmodelsファイルを読み込んでいる。
#ここは投稿する時の定義をしています。
genre = Genre.objects.get(id=1)
p = PostInfo(
    genre_id=genre,
    post_title="お金について",
    post_content="お金引き寄せる方法",
    reaction_count=1,
)

p.save()

