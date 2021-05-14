from django.shortcuts import render
from ipl.models import *
from ipl.forms import *

# Create your views here.

def home_page(request):
	return render(request = request, template_name = 'ipl/homepage.html')

def team_list(request):
	return render(request = request, template_name = 'ipl/TeamList.html')

def add_DelhiCapitals(request):
	players_form = DelhiCapitalsForm()

	if request.method == 'POST':
		form_data = DelhiCapitalsForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form}

	return render(request = request, template_name = 'ipl/DelhiCapitals.html', context= my_dict)

def add_MumbaiIndians(request):
	players_form = MumbaiIndiansForm()

	if request.method == 'POST':
		form_data = MumbaiIndiansForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form}

	return render(request = request, template_name = 'ipl/MumbaiIndians.html', context= my_dict)

def add_CSK(request):
	players_form = CSKForm()

	if request.method == 'POST':
		form_data = CSKForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form}

	return render(request = request, template_name = 'ipl/CSK.html', context= my_dict)

def add_PunjabKings(request):
	players_form = PunjabKingsForm()

	if request.method == 'POST':
		form_data = PunjabKingsForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form}

	return render(request = request, template_name = 'ipl/PunjabKings.html', context= my_dict)

def add_KKR(request):
	players_form = KKRForm()

	if request.method == 'POST':
		form_data = KKRForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form}

	return render(request = request, template_name = 'ipl/KKR.html', context= my_dict)

def add_SRH(request):
	players_form = SRHForm()

	if request.method == 'POST':
		form_data = SRHForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form}

	return render(request = request, template_name = 'ipl/SRH.html', context= my_dict)

def add_RR(request):
	players_form = RRForm()

	if request.method == 'POST':
		form_data = RRForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form}

	return render(request = request, template_name = 'ipl/RR.html', context= my_dict)

def add_RCB(request):
	players_form = RCBForm()

	if request.method == 'POST':
		form_data = RCBForm(request.POST)
		if form_data.is_valid():
			form_data.save(commit = True)

	my_dict  = {'players_form': players_form , }

	return render(request = request, template_name = 'ipl/RCB.html', context= my_dict)


def ipl_players_list(request):
	DelhiCapitals_data = DelhiCapitalsTable.objects.all()
	MumbaiIndians_data = MumbaiIndiansTable.objects.all()
	CSK_data = CSKTable.objects.all()	
	PunjabKings_data = PunjabKingsTable.objects.all()
	KKR_data = KKRTable.objects.all()
	SRH_data = SRHTable.objects.all()
	RR_data = RRTable.objects.all()
	RCB_data = RCBTable.objects.all()

	my_dict = {'DelhiCapitals_data': DelhiCapitals_data,'MumbaiIndians_data': MumbaiIndians_data, 'CSK_data':CSK_data, 'PunjabKings_data': PunjabKings_data ,  'KKR_data':KKR_data,
	'SRH_data': SRH_data,'RR_data':RR_data, 'RCB_data':RCB_data}

	return render(request = request, template_name = 'ipl/complete_data.html', context = my_dict)


