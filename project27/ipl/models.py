from django.db import models

# Create your models here.

class IPL_Team(models.Model):
	name = models.CharField(max_length=20)
	age = models.IntegerField()
	country = models.CharField(max_length=20)
	marital_status = models.CharField(max_length=20)
	form = models.CharField(max_length=20)

	class Meta:
		abstract = True

class DelhiCapitalsTable(IPL_Team):
	Team_name  = 'DelhiCapitals'


class MumbaiIndiansTable(IPL_Team):
	Team_name  = 'MumbaiIndians'
 
class CSKTable(IPL_Team):
	Team_name  = 'CSK'

class PunjabKingsTable(IPL_Team):
	Team_name  = 'PunjabKings'

class KKRTable(IPL_Team):
	Team_name  = 'KKR'

class SRHTable(IPL_Team):
	Team_name  = 'Team_name'

class RRTable(IPL_Team):
	Team_name  = "RR"


class RCBTable(IPL_Team):
	Team_name  = 'RCB'