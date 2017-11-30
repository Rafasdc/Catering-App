from django.contrib import admin

from .models import Event, ItemInventory, Item, EventInventoryInstance, EventQuantity

# admin.site.register(Event)
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event_type','date', 'startTime', 'endDate', 'endTime', 'numGuests',
     'location', 'menu', 'status', 'id',)
    list_filter = ('date', 'startTime', 'status')

@admin.register(ItemInventory)
class ItemInventoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

@admin.register(EventQuantity)
class EventQuantityAdmin(admin.ModelAdmin):
    pass

@admin.register(EventInventoryInstance)
class EventInventoryInstance(admin.ModelAdmin):
    pass


