from django.contrib import admin
from home import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "email",
        "status",
        "date",
    ]

admin.site.register(models.Student)