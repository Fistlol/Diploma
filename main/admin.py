from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


class CustomUserAdmin(UserAdmin):
    model = models.User
    list_display = ("username", "email", "first_name", "last_name", "is_staff", "age", "phone", "address")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email", "age", "phone", "address")
    ordering = ("username", "first_name", "last_name", "email", "age", "phone", "address")

    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (("Personal info"), {"fields": ("first_name", "last_name", "email", "age", "phone", "address")}),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )


admin.site.register(models.Company)
admin.site.register(models.Food)
admin.site.register(models.Diet)
admin.site.register(models.User, CustomUserAdmin)
admin.site.register(models.UserPlan)
admin.site.register(models.Plan)
