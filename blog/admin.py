from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


class PostBlogAdminForm(forms.ModelForm):
    content = forms.CharField(label='Текст', widget=CKEditorUploadingWidget())

    class Meta:
        model = PostBlog
        fields = '__all__'


class PostBlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PostBlogAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    list_filter = ('category', 'tags',)
    readonly_fields = ('views', 'created_at', 'get_photo')
    fields = ('title', 'slug', 'category', 'tags', 'content', 'photo', 'get_photo', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Картинка'


class CategoryBlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class TagBlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}




admin.site.register(CategoryBlog, CategoryBlogAdmin)
admin.site.register(TagBlog, TagBlogAdmin)
admin.site.register(PostBlog, PostBlogAdmin)
