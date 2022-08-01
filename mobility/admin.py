from django.contrib import admin
from mobility.models import *
# Register your models here.

@admin.register(Post)
class QuillPostAdmin(admin.ModelAdmin):
    list_display = ("title", "text",)
    prepopulated_fields = {"slug": ("title",)}