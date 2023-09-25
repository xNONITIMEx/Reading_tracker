from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import ReaderCreationForm, ReaderChangeForm
from .models import Reader


class ReaderAdmin(UserAdmin):
    add_form = ReaderCreationForm
    form = ReaderChangeForm
    model = Reader

    list_display = ('email', 'date_joined','is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')})
    )
    add_fieldsets = (
        (None, {'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'is_staff', 'is_astive', 'groups', 'user_permissions')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(Reader, ReaderAdmin)