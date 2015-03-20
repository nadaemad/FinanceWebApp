from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
from django.template import Context
from app1.models import user

def home3(request, u_id):
	u = user.objects.get(id=u_id)
	return render_to_response('homepage3.html', {'u': u}, context_instance=RequestContext(request))

def editprofile(request, u_id):
	u = user.objects.get(id=u_id)
	return render_to_response('editprofile.html', {'u': u}, context_instance=RequestContext(request))   

def myaccount(request, u_id):
	u = user.objects.get(id=u_id)
	return render_to_response('myaccount.html', {'u': u}, context_instance=RequestContext(request))   

def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))


def home2(request):

	if request.POST:
		email = request.POST['email']
		firstname = request.POST['fn']
		lastname = request.POST['ln']
		password = request.POST['pass']
		confirmpassword = request.POST['cpass'] 
		companyname = request.POST['cname']
		dateoforigin = request.POST['date']

		u = user(user_email=email, first_name=firstname, Last_name=lastname, password=password, confirm_password=confirmpassword, company_name=companyname, company_date_of_origin=dateoforigin)
		u.save()
		return render_to_response('homepage3.html', {'u':u}, context_instance=RequestContext(request))
	else:
		return HttpResponse("hey")

def signup(request):

	return render_to_response('signup.html', {}, context_instance=RequestContext(request))