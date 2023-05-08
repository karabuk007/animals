from django.contrib import admin

from .models import *
class Main_PageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'photo')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')


admin.site.register(Dogs, Main_PageAdmin)
admin.site.register(Cats, Main_PageAdmin)
admin.site.register(Classmates, Main_PageAdmin)
admin.site.register(MainPage, Main_PageAdmin)


