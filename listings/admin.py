from django.contrib import admin
from .models import PostJob


class PostJobAdmin (admin.ModelAdmin):
    list_display = ('id', 'job', 'department', 'location', 'status', 'job_published')
    list_display_links = ('id', 'job')
    list_editable = ('status', 'job_published',)
    list_per_page = 25


admin.site.register(PostJob, PostJobAdmin)
