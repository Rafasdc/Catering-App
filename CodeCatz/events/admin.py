from django.contrib import admin

from .models import Event

# admin.site.register(Event)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'startTime', 'numGuests',
     'location', 'status', 'id')
    list_filter = ('date', 'startTime', 'status')
