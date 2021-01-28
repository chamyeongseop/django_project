from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    # 게시글 데이터가 생성될 때, 현재 시간이 등록 됨
    created_at = models.DateTimeField(auto_now=True)
    


#
# class Post(models.Model):
#     title = models.CharField(max_length=30)
#     content = models.TextField()
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)