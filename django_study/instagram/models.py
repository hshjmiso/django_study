from django.conf import settings
from django.db import models

# from django.contrib.auth.models import User # 추천하지 않는다 변하거나 중복될 가능성이 크기 때문에

class Post(models.Model):
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)(null=True)
    message = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True) # tag가 밑에 있을 경우 문자열로 대체 할 수 있다.
    is_public = models.BooleanField(default=False, verbose_name="공개여부")
    created_at = models.DateTimeField(auto_now_add=True) # https://tomining.tistory.com/145 auto_now_add vs auto_now
    updated_at = models.DateTimeField(auto_now=True)

    # Java의 toString
    def __str__(self):
        # return f"Custom Post Object ({self.id})"
        # return "Custom Post Object ({})".format(self.id)
        return self.message
    
    def message_length(self):
        return len(self.message)
    message_length.short_description = "메세지 글자수"

    class Meta:
        ordering = ['-id']

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             limit_choices_to={'is_public': True}) # post_id 필드
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    # post_set = models.ManyToManyField(Post)

    def __str__(self):
        return self.name