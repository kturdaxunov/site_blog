from django.contrib import admin
from .models import *
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe


class ProjectPortfolioAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = ProjectPortfolio
        fields = '__all__'


class ProjectPortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = ProjectPortfolioAdminForm
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'category', 'created_at', 'get_photo', 'views')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content',)
    list_filter = ('category',)
    readonly_fields = ('views', 'get_photo')
    fields = ('title', 'slug', 'category', 'content', 'link', 'photo', 'photo2', 'photo3', 'get_photo', 'views', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Изоброжение'


class CategoryPortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


admin.site.register(CategoryPortfolio, CategoryPortfolioAdmin)
admin.site.register(ProjectPortfolio, ProjectPortfolioAdmin)

admin.site.site_title = 'Управление сайтом'
admin.site.site_header = 'Управление сайтом'
