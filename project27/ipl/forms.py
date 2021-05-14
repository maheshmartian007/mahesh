from ipl.models import *
from django import forms

class DelhiCapitalsForm(forms.ModelForm):
	class Meta:
		model = DelhiCapitalsTable
		fields = '__all__'

class MumbaiIndiansForm(forms.ModelForm):
	class Meta:
		model = MumbaiIndiansTable
		fields = '__all__'

class CSKForm(forms.ModelForm):
	class Meta:
		model = CSKTable
		fields = '__all__'

class PunjabKingsForm(forms.ModelForm):
	class Meta:
		model = PunjabKingsTable
		fields = '__all__'

class SRHForm(forms.ModelForm):
	class Meta:
		model = SRHTable
		fields = '__all__'

class KKRForm(forms.ModelForm):
	class Meta:
		model = KKRTable
		fields = '__all__'

class RRForm(forms.ModelForm):
	class Meta:
		model = RRTable
		fields = '__all__'

class RCBForm(forms.ModelForm):
	class Meta:
		model = RCBTable
		fields = '__all__'

