from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from app1.models import *
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, RequestContext
from django.template import Context
from app1.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User


def home3(request, u_id):
	u = User.objects.get(id=u_id)
	return render_to_response('homepage3.html', {'u': u}, context_instance=RequestContext(request))


def editprofile(request, u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)
	return render_to_response('editprofile.html', {'u': u, 'u2': u2}, context_instance=RequestContext(request))   


def myaccount(request, u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)
	if request.POST:
		firstname = request.POST['firstname']
		u.firstname = firstname
		u.save()
	return render_to_response('myaccount.html', {'u': u, 'u2': u2}, context_instance=RequestContext(request))   


def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))


def newproject(request, u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)
	return render_to_response('newproject.html', {'u': u, 'u2': u2}, context_instance=RequestContext(request))


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


def myprojects(request, u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)

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
		p = Project(pname=pname, prof=gp ,client=u2)
		p.save()
		j=0;
		while(j<i):
			e = Expense(ename = enames[j], eamount = eamounts[j])
			e.save()
			p.exp.add(e)
			j+=1

		p.save()
		print Project.objects.all()
	return render_to_response('myprojects.html', {'projects':Project.objects.all(), 'u': u, 'u2': u2}, context_instance=RequestContext(request))


def notauser(request):
	return render_to_response('notauser.html', {}, context_instance=RequestContext(request))


def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            registered = True
        else:
            print user_form.errors, profile_form.errors
    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)


def user_login(request):

    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                u2 = UserProfile.objects.get(user=user)
                return render_to_response('home.html', {'user':user, 'user2':u2}, context)
            else:
                return HttpResponse("Your financeweb account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render_to_response('login.html', {}, context)


@login_required
def restricted(request):
    return HttpResponse("Since you're logged in, you can see this text!")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('home')

def deleteproject(request,p_id,u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)
	
	if request.POST:
		project= Project.objects.get(id=p_id)
		project.delete()
		return render_to_response('myprojects.html', {'projects':Project.objects.all(), 'u': u, 'u2': u2}, context_instance=RequestContext(request))


def ourapp(request):
	return render_to_response('ourapp.html', {}, context_instance=RequestContext(request))


def ourfeatures(request):
	return render_to_response('ourfeatures.html', {}, context_instance=RequestContext(request))




















