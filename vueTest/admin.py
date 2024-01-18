from django.contrib import admin

from vueTest.models import Worker


# Register your models here.
@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    search_fields = ['name', 'surname', 'phone', 'email']
    ordering = ['surname']
