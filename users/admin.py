from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Department, UserRole


class CustomUserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
            'mobile',
            'gender',
            'address',
            'city',
            'state',
            'country',
            'supervisor',
            'role',
            'dept',
            'profile_pic',
        )}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
            'groups',
            'user_permissions',
        )}),
        ('Important dates', {'fields': (
            'last_login',
            'date_joined',
        )}),
    )
    add_fieldsets = (
        (
            None,
            {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2')
            }
        ),
    )

    list_display = ('email', 'first_name', 'last_name','dept', 'role', 'is_staff',
                    'last_login')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'role')
    search_fields = ('email','dept', 'role')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

    class Meta:
        model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserRole)
admin.site.register(Department)