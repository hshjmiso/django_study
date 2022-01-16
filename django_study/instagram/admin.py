from django.contrib import admin
from .models import Post, Comment

# Register your models here.
# 1
#admin.site.register(Post)

# 2
# class PostAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Post, PostAdmin)

# 3
@admin.register(Post) #Wrapping
class PostAdmin(admin.ModelAdmin):
    # pass
    list_display = ['id', 'message', 'message_length', 'is_public', 'created_at', 'updated_at']
    list_display_links = ['message']
    list_filter = ['created_at', 'is_public']
    search_fields = ['message']

    def message_length(self, post):
        # return len(post.message)
        return f"{len(post.message)} 글자" 

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass