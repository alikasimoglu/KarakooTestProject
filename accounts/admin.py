from django.contrib import admin
from accounts.models import User, Employee, Customer
from config.settings import ADMIN_ORDERING


def get_app_list(self, request):
    app_dict = self._build_app_dict(request)
    for app_name, object_list in ADMIN_ORDERING:
        app = app_dict[app_name]
        app['models'].sort(key=lambda x: object_list.index(x['object_name']))
        yield app


admin.AdminSite.get_app_list = get_app_list


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["email", "date_joined", "is_employee", "is_customer"]
    readonly_fields = ("date_joined", "last_login", )
    fieldsets = (
        ("LOGIN INFORMATIONS", {
            "fields": ("email", "password")
        }),
        ("STATUS AND PERMISSIONS", {
            "fields": ("is_active", "is_employee", "is_customer", "is_staff", "is_superuser", "groups", "user_permissions", "date_joined", "last_login")
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ["profile", "first_name", "last_name", "date_joined", "is_active"]
    readonly_fields = ("date_joined", "updated_on")
    fieldsets = (
        ("USER INFORMATIONS", {
            "fields": ("profile", "first_name", "last_name", "phone")
        }),
        ("STATUS AND TIME INFO", {
            "fields": ("is_active", "date_joined", "updated_on")
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ["profile", "first_name", "last_name", "phone", "date_joined", "is_active"]
    readonly_fields = ("date_joined", "updated_on")
    fieldsets = (
        ("USER INFORMATIONS", {
            "fields": ("profile", "first_name", "last_name", "phone", "representative_name", "representative_phone")
        }),
        ("STATUS AND TIME INFO", {
            "fields": ("is_active", "date_joined", "updated_on")
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True
