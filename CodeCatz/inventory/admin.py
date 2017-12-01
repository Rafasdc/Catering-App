from django.contrib import admin
from .models import ItemInventory, Item, EventInventoryInstance, EventQuantity



class IngredientQuantityInline(admin.TabularInline):
    model = EventQuantity

# Register your models here.
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
    inlines = (IngredientQuantityInline,)
