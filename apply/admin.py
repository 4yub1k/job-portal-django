from django.contrib import admin
from .models import ApplicantForm
from .models import Review


class ApplicantFormAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email")
    list_display_links = ("id", "name")
    list_per_page = 25


admin.site.register(ApplicantForm, ApplicantFormAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "reviewd", "ratings", "remarks")
    list_display_links = ("id", "name")
    list_per_page = 25


admin.site.register(Review, ReviewAdmin)
