from django.shortcuts import render
from catering.models import TotalEvent


# Create your views here.

def database(request):
	customerid= request.GET.get('cid')
	eventid= request.GET.get('eid')
	guests= request.GET.get('g')
	loc= request.GET.get('location')
	strtime= request.GET.get('strtime')
	evntdate= request.GET.get('evedate')
	c= TotalEvent(CustomerID=customerid,eventID=eventid,eventPlace=loc,eventStartTime=strtime,eventDate=evntdate,Guests=guests)
	c.save()
	
	return render(request,'catering/index.html')

def schedule(request):
	return render(request,'catering/schedule.html')