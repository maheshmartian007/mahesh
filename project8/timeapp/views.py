from django.shortcuts import render

import datetime
# Create your views here.


def server_time(request):
	server_time = datetime.datetime.now()
	print(server_time)
	dict = {'time':server_time}
	print(dict)

	return render(request = request, template_name = 'timeapp/time.html',context = dict)


