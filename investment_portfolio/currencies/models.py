from django.core.urlresolvers import reverse
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel, SoftDeletableModel
from model_utils import Choices, FieldTracker


@python_2_unicode_compatible
class Base(SoftDeletableModel, TimeStampedModel):
	
	tracker = FieldTracker()

	class Meta:
		abstract = True


@python_2_unicode_compatible
class Currency(Base):

	# First Name and Last Name do not cover name patterns
	# around the globe.
	name = models.CharField(_('Name of currency'), blank=True, max_length=255, 
													unique=True)
	symbol = models.CharField(_('Symbol of currency'), blank=False, null=False, 
														max_length=10, unique=True)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('currencies:currencies_detail', kwargs={'name': self.name})


@python_2_unicode_compatible
class CurrencyData(Base):
	
	currency = models.ForeignKey(Currency, blank=False, null=False)
	
	rank = models.PositiveSmallIntegerField(blank=False, null=False)
	price_usd = models.FloatField(blank=False, null=False)
	price_btc = models.FloatField(blank=False, null=False)
	daily_volume_usd = models.FloatField(blank=False, null=False)
	market_cap_usd = models.FloatField(blank=False, null=False)
	available_supply = models.FloatField(blank=False, null=False)
	total_supply = models.FloatField(blank=False, null=False)
	max_supply = models.FloatField(blank=False, null=False)
	percent_change_1h = models.FloatField(blank=False, null=False)
	percent_change_24h = models.FloatField(blank=False, null=False)
	percent_change_7d = models.FloatField(blank=False, null=False)
	last_updated = models.PositiveSmallIntegerField(blank=False, null=False)


	def __str__(self):
		return '{} : {}'.format(
			self.currency.name,
			self.created
			)

	def get_absolute_url(self):
		return reverse('currencies:currencies_data_detail', kwargs={'pk': self.pk})