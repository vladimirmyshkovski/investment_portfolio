from django import forms
from .models import PortfolioItem
from investment_portfolio.currencies.models import Currency
from djmoney.forms.fields import MoneyField

class PortfolioItemForm(forms.ModelForm):

	invest_date = forms.DateField()
	amount = forms.FloatField()
	price = MoneyField()

	class Meta:
		model = PortfolioItem
		fields = ['currency']

	def __init__(self, *args, **kwargs):
		super(PortfolioItemForm, self).__init__(*args, **kwargs)
		self.fields['currency'].queryset = Currency.objects.all()