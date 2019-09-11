from django.contrib import admin

# Register your models here.

from django.contrib import admin
 
# Register your models here.
from blog.models import Category, Post
 
class ChoiceInLine(admin.StackedInline):
    model = Category 
    extra = 3
  
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (Category, {'fields': ['catID']}),
    ]
    inlines = [ChoiceInLine]