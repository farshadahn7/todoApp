from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'status', 'created_at')
    search_fields = ('title',)
    list_filter = ('status',)
