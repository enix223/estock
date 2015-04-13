#encoding: utf-8

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import forms

from console.models import NewStockRate

_PLATE = ('cyb', 'zxb', 'sh', 'sz',)

class CombinationForm(forms.Form):
	szquota = forms.IntegerField()
	shquota = forms.IntegerField()
	cash    = forms.DecimalField(min_value = 1.0)

@login_required
def list(request):
	if 'plate' not in request.GET:
		stocks = NewStockRate.objects.all()
	else:
		plate = request.GET['plate']
		if(plate in _PLATE):
			stocks = NewStockRate.objects.filter(plate=plate)
		else:
			stocks = NewStockRate.objects.all()		

	return render(request, 'newstock/list.html', {'stocks': stocks,})

@login_required
def combine(request):	
	if(request.method == 'POST'):
		form = CombinationForm(request.POST)
		if(form.is_valid()):
			# TO-DO
			return render(request, 'newstock/combine-result.html')
	else:
		form = CombinationForm()
	
	return render(request, 'newstock/combine.html', {'form': form,})