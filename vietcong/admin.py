from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjUserAdmin
from django.contrib.auth.models import Group

from .models import User


class UserAdmin(DjUserAdmin):
    list_display = ['email', 'name',
                    'is_active', 'is_trusted', 'is_admin']
    list_filter = ['is_active', 'is_trusted', 'is_admin']
    filter_horizontal = []
    ordering = ['-is_admin', 'name']
    search_fields = ['email', 'name']

    fieldsets = [
        (None, {'fields': ['email', 'name', 'password',
                           'is_active', 'is_trusted', 'is_admin',
                           'date_joined', 'last_login',
                          ],
                }),
    ]
    add_fieldsets = [
        (None, {'fields': ['email', 'name',
                           'is_active', 'is_trusted',
                           'password1', 'password2',
                          ],
                }),
    ]
    readonly_fields = ['date_joined', 'last_login']


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
