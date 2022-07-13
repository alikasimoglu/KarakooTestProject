from django.contrib import admin
from mainsite.models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["company_name", "employee", "company_email", "date_created", "is_active", "is_accepted", "is_email_sent", "is_registered"]
    readonly_fields = ("date_created", "updated_on")
    fieldsets = (
        ("USER INFORMATIONS", {
            "fields": ("employee", "company_name", "company_email", "company_phone", "additional_info")
        }),
        ("STATUS AND TIME INFO", {
            "fields": ("is_active", "is_accepted", "is_email_sent", "is_registered", "date_created", "updated_on")
        })
    )

    def has_delete_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True
