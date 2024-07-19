from django.contrib import admin
from . import models

class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'note', 'created_at', 'updated_at')
    search_fields = ('title', 'note')
    list_filter = ('created_at', 'updated_at')

admin.site.register(models.Notes, NotesAdmin)