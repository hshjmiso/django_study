from django.db import models

class Post(models.Model):
    message = models.TextField()
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