from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
import reversion

class Type(models.Model):
	name = models.CharField(_('Name'), max_length=200, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Type')
		verbose_name_plural = _('Types')

	def get_absolute_url(self):
		return reverse('type-detail', kwargs={'pk': self.pk})

	def get_edit_url(self):
		return reverse('type-edit', kwargs={'pk': self.pk})


class Building(models.Model):
	name = models.CharField(_('Name'), max_length=200, blank=True)
	number = models.CharField(_('Number'), max_length = 30, blank = True)
	street = models.CharField(_('Street'), max_length = 100, blank = True)
	zipcode = models.CharField(_('ZIP code'), max_length = 5, blank = True)
	city = models.CharField(_('City'), max_length = 100, blank = True)
	state = models.CharField(_('State'), max_length = 100, blank = True)
	country = models.CharField(_('Country'), max_length = 100, blank = True)
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Building')
		verbose_name_plural = _('Buildings')

	def get_absolute_url(self):
		return reverse('building-detail', kwargs={'pk': self.pk})

	def get_edit_url(self):
		return reverse('building-edit', kwargs={'pk': self.pk})


class Room(models.Model):
	name = models.CharField(_('Name'), max_length=200, blank=True)
	building = models.ForeignKey(Building)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Room')
		verbose_name_plural = _('Rooms')

	def get_absolute_url(self):
		return reverse('room-detail', kwargs={'pk': self.pk})

	def get_edit_url(self):
		return reverse('room-edit', kwargs={'pk': self.pk})

class Manufacturer(models.Model):
	name = models.CharField(_('Manufacturer'), max_length=200, blank=True)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Manufacturer')
		verbose_name_plural = _('Manufacturers')

	def get_absolute_url(self):
		return reverse('manufacturer-detail', kwargs={'pk': self.pk})

	def get_edit_url(self):
		return reverse('manufacturer-edit', kwargs={'pk': self.pk})

class Device(models.Model):
	name = models.CharField(_('Name'), max_length=200)
	buildnumber = models.CharField(_('Buildnumber'), max_length=50, unique=True)
	serialnumber = models.CharField(_('Serialnumber'), max_length=50, unique=True)
	macaddress = models.CharField(_('MAC Address'), max_length=40, unique=True)
	manufacturer = models.ForeignKey(Manufacturer, blank=True, null=True)
	hostname = models.CharField(_('Hostname'), max_length=40, blank=True)
	description = models.CharField(_('Description'), max_length=1000, blank=True)
	devicetype = models.ForeignKey(Type, blank=True, null=True)
	room = models.ForeignKey(Room, blank=True, null=True)

	owner = models.ForeignKey(User, blank=True, null=True)


	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('Device')
		verbose_name_plural = _('Devices')

	def get_absolute_url(self):
		return reverse('device-detail', kwargs={'pk': self.pk})

	def get_edit_url(self):
		return reverse('device-edit', kwargs={'pk': self.pk})


reversion.register(Device)