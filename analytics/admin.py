from django.contrib import admin
from . models import PageVisit, PageViewsAnalytics, TextMessage

class PageVisitAdmin(admin.ModelAdmin):
    list_display = ('count', 'ip', 'timestamp')

class TextMessageAdmin(admin.ModelAdmin):
    list_display = ('text', 'ip', 'timestamp')


admin.site.register(PageVisit, PageVisitAdmin)
admin.site.register(TextMessage, TextMessageAdmin)
admin.site.register(PageViewsAnalytics)