import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mind_ch_db.settings')
from django import setup
setup()

from mind_ch_db.models import PostInfo

# 全て取得
"""postinfos = PostInfo.objects.all()
for PostInfo in postinfos:
    print(PostInfo.post_title, PostInfo.post_content, PostInfo.reaction_count,)

print('/////////////////////////////////////////////')"""
#選択された、投稿の詳細情報を表示
"""
postinfo = PostInfo.objects.get(id=1)
print(postinfo.post_title, postinfo.post_content, postinfo.reaction_count,)
"""

postinfos = PostInfo.objects.filter(post_title='お金について').all()
for postinfo in postinfos:
    print(postinfo.post_title, postinfo.post_content, postinfo.reaction_count)
