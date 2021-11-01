from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter= ('status', 'created', 'publish', 'author')
    search_fields  = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)} #автоматически формирует краткий заголовок
    raw_id_fields = ('author',) #позволяет, при создании выбора автора заголовка не открывать выпадающий список, а выбрать в отдельном окне автора
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')