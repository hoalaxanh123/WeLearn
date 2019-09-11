from django.contrib import admin
from .models import *
# Register your models here.
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title','description','dateCreate']
    list_filter = ['dateCreate']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','subjectID','description']
    list_filter = ['subjectID']
    search_fields = ['title']

class PostAdmin(admin.ModelAdmin):
    list_display = ['title','catID','description','dateCreate','creator','viewCount']
    list_filter = ['catID']
    search_fields = ['title']

admin.site.register(Post,PostAdmin)
admin.site.register(Subject,SubjectAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Log)
admin.site.register(FeedBack)
