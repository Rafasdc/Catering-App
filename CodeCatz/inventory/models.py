from django.db import models
from events.models import Event
from django.utils.translation import ugettext_lazy as _
# Create your models here.
# Inventory for Event
class Item(models.Model):
	name = models.CharField(_("Name of Item"), max_length=100)
	description = models.CharField(verbose_name=_(u'Description'), max_length=64, null=True, blank=True)
	part_number = models.CharField(verbose_name=_(u'Item number'), max_length=32, null=True, blank=True)
	notes = models.TextField(verbose_name=_(u'Notes'), null=True, blank=True)

	class Meta:
		verbose_name = _(u'Item')
		verbose_name_plural = _(u'Items')

	def __str__(self):
		return self.name


class ItemInventory(models.Model):
	item = models.ForeignKey(Item)
	amountAvailable = models.IntegerField(_('Amount Available in Inventory'))
	amountUnavailable = models.IntegerField(_('Amount Used from Inventory'))


	def __str__(self):
		return self.item.name

	class Meta:
		verbose_name = _(u'Item inventory')
		verbose_name_plural = _(u'Item inventories')


class EventQuantity(models.Model):
	item = models.ForeignKey(Item)
	amount = models.DecimalField(_('Amount necessary for event.'), max_digits=10, decimal_places=2, default=0.00)
	event = models.ForeignKey('EventInventoryInstance')

	def __str__(self):
		return "{:.2f} {:s}".format(self.amount, self.item.name)

	class Meta:
		verbose_name = _(u'Event Quantity')
		verbose_name_plural = _(u'Event Quantities')


class EventInventoryInstance(models.Model):
	items = models.ManyToManyField(Item, through=EventQuantity)
	event = models.ForeignKey(Event)

	class Meta:
		verbose_name = _(u'Event Inventory')
		verbose_name_plural = _(u'Event Inventories')
		