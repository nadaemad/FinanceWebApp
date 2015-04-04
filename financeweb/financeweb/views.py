from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext

from app1.models import *

from django.contrib.auth import authenticate, login


def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))

def home2(request):
	return render_to_response('homepage2.html', {}, context_instance=RequestContext(request))

def login_user(request):
    context = RequestContext(request)
    #language = 'en-gb'
    #session_language = 'en-gb'

    #Here the user log ins and starts authentication w hawelt a3mel session w ma3rafsh keda sahh wala la2

    state = "Please login below..."
    username = password = ''
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            #language = request.COOKIES['language']

            if user.is_active:
                u = user.objects.get(username=request.POST['username'])
                login(request, user)
                if u.password == request.POST['password']:
                    request.session['user'] = u.email
                    state = "You're successfully logged in!"
                    return render_to_response('home.html',{'state':state, 'username': username}, context)
            else:
                state = "Your account is not active, please contact the site admin."
        else:
            state = "Your username and/or password were incorrect."
            
    return render_to_response('signin.html',{'state':state, 'username': username}, context)

def abc(request):

	if request.POST:
		email = request.POST['email']
		username = request.POST['username']
		firstname = request.POST['fn']
		lastname = request.POST['ln']
		password = request.POST['pass']
		confirmpassword = request.POST['cpass'] 
		companyname = request.POST['cname']
		dateoforigin = request.POST['date']

		u = user(user_email=email, user_name=username, first_name=firstname, Last_name=lastname, password=password, confirm_password=confirmpassword, company_name=companyname, company_date_of_origin=dateoforigin)
		u.save()
		return render_to_response('homepage2.html', {}, context_instance=RequestContext(request))

	else:
		return render_to_response('signup.html', {}, context_instance=RequestContext(request))



def newproject(request):
	return render_to_response('newproject.html', {}, context_instance=RequestContext(request))

def viewproject(request, post_id):
	p = Project.objects.get(id=post_id)
	exp = Project.objects.get(id=post_id).exp.all()

	return render_to_response('viewproject.html', {'p':p, 'e':exp}, context_instance=RequestContext(request))


def updateproject(request, post_id):
	p = Project.objects.get(id=post_id)
	gp = Project.objects.get(id=post_id).prof
	exp = Project.objects.get(id=post_id).exp.all()

	if request.POST:
		nname = request.POST['newname']
		p.pname = nname;
		p.save()

		nprof = request.POST['newprofit']
		gp.pamount = nprof;
		gp.save()


		for e in exp:
			name = request.POST['exp_name[%d]'%e.id]
			amount = request.POST['exp_amount[%d]'%e.id]
			e.ename = name
			e.eamount = amount
			e.save()

		#part of adding expenses men awel wegdeed#
		enames = []
		eamounts = []
		done = False
		i=0
		while(not done):
			try:
				enames.append(request.POST['ename[%d]'%i])
				eamounts.append(request.POST['eamount[%d]'%i])
				i+=1
			except:
				done=True

		j=0;
		while(j<i):
			e = Expense(ename = enames[j], eamount = eamounts[j])
			e.save()
			p.exp.add(e)
			j+=1

		p.save()

		return render_to_response('viewproject.html', {'p':p, 'e':exp}, context_instance=RequestContext(request))

	else:
		return render_to_response('updateproject.html', {'p':p, 'e':exp}, context_instance=RequestContext(request))


def myprojects(request):

	if request.POST:
		pname = request.POST['pname']
		pamount = request.POST['pamount']
		enames = []
		eamounts = []
		done = False
		i=0
		while(not done):
			try:
				enames.append(request.POST['ename[%d]'%i])
				eamounts.append(request.POST['eamount[%d]'%i])
				i+=1
			except:
				done=True
		print 'enames', enames
		print 'eamounts', eamounts

		gp = Gprofit(pamount = pamount)
		gp.save()
		p = Project(pname=pname, prof=gp)
		p.save()
		j=0;
		while(j<i):
			e = Expense(ename = enames[j], eamount = eamounts[j])
			e.save()
			p.exp.add(e)
			j+=1

		p.save()
		print Project.objects.all()
	return render_to_response('myprojects.html', {'projects':Project.objects.all()}, context_instance=RequestContext(request))
	
