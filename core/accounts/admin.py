from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('email', 'is_active', 'is_superuser',
                    'is_staff', 'is_verified')
    list_filter = ('email', 'is_superuser', 'is_staff', 'is_verified')
    search_fields = ('email',)
    ordering = ('email',)
    # to show the informathin of the user in admin panel
    fieldsets = (
        ('Authentication', {'fields': ('email', 'password')}),
        # Add permissions if you want to manage them
        ('Permissions', {'fields': ('is_active', 'is_staff',
                                    'is_superuser', 'is_verified', 'user_permissions')}),
        ('important date', {'fields': ('last_login',)}),

    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "password1", "password2", 'is_active', 'is_staff', 'is_verified',
                                    'is_superuser']
            },
        ),
    ]


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
