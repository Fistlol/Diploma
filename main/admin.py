from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models

admin.site.register(models.Company)
admin.site.register(models.Food)
admin.site.register(models.Diet)
admin.site.register(models.User, UserAdmin)
admin.site.register(models.UserPlan)
admin.site.register(models.Plan)
