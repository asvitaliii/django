from django.contrib import admin
from .models import Verse, Author


class VerseModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'author']
    list_display_links = ['id']
    list_editable = ['name']

    list_filter = ['name', 'author']
    search_fields = ['name', 'author__name']

    class Meta:
        model = Verse


# admin.site.register(Verse)
admin.site.register(Author)
admin.site.register(Verse, VerseModelAdmin)

