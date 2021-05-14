from django.urls import path
from ipl import views

urlpatterns = [
	path('delhicapitals/', views.add_DelhiCapitals),
	path('mumbaiindians/', views.add_MumbaiIndians),
	path('csk/', views.add_CSK),
	path('punjabkings/', views.add_PunjabKings),
	path('kkr/', views.add_KKR),
	path('srh/', views.add_SRH),
	path('rr/', views.add_RR),
	path('rcb/', views.add_RCB),
	path('homepage/', views.home_page),
	path('teamlist/', views.team_list),
	path('iplteamplayerslist/', views.ipl_players_list),
]