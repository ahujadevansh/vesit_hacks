from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Department, UserRole

admin.AdminSite.site_header = "e_pars-Admin"
admin.AdminSite.site_title = "E-PARS Site admin"
admin.AdminSite.index_title = "E-PARS site adminstration"

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
            'ratings',
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