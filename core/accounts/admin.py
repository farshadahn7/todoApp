from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'email', 'created_at')
    list_filter = ('username', 'email', 'is_staff')
    fieldsets = (
        ('authentication', {'fields': ('username', 'email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2')}),
    )
    search_fields = ('username', 'email')
