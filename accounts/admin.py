from django.contrib import admin
from accounts.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "date_joined"]
    readonly_fields = ("date_joined", "last_login", )
    fieldsets = (
        (None, {
            "fields": ("email", "password", "first_name", "last_name")
        }),
        ("GENEL BİLGİLER", {
            "fields": ("is_active", "is_employee", "is_customer", "is_staff", "is_superuser", "groups", "user_permissions", "date_joined", "last_login")
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True
