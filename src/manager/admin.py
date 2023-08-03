from django.contrib import admin

from manager.models import Book, Comment


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1


class BookAdmin(admin.ModelAdmin):
    inlines = [CommentInline]

admin.site.register(Book)
admin.site.register(Comment)
