from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title', )}  # слаг формируется сам при заполнении тайтла
    raw_id_fields = ['author']  # при создании поста автор теперь с поисковом окне а не в выпадающем
    date_hierarchy = 'publish'  # добавилась навигационная ссылка по датам
    ordering = ['status', 'publish']
