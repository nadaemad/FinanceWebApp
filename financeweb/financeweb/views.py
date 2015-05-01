from django.template import Context, RequestContext
from app1.models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
from app1.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.views import password_reset, password_reset_confirm
from datetime import datetime
import calendar

def reset(request):
	return password_reset(request, template_name='reset.html', email_template_name='reset_email.html', 
		subject_template_name='reset_subject.txt', post_reset_redirect= reverse('success'))

def reset_confirm(request, uidb64=None, token=None):
	return password_reset_confirm(request, template_name='reset_confirm.html',
		uidb36=uidb36, token=token, post_reset_redirect=reverse('success'))

def success(request):
	return render(request, "success.html")

def home3(request, u_id):
	u = User.objects.get(id=u_id)
	return render_to_response('homepage3.html', {'u': u}, context_instance=RequestContext(request))


def editprofile(request, u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)
	return render_to_response('editprofile.html', {'u': u, 'u2': u2}, context_instance=RequestContext(request))   


def myaccount(request, u_id):
	# u = User.objects.get(id=u_id)
	# u2 = UserProfile.objects.get(user=u)
	if request.POST:
		user = request.user
		user.first_name = request.POST['firstname']
		user.save()

		user.last_name = request.POST['lastname']
		user.save()

		user.email = request.POST['email']
		user.save()

		user.user_profile.companyname = request.POST['companyname']
		user.save()

		user.password = request.POST['newpassword']
		user.save()

	return render_to_response('myaccount.html', {'u': request.user, 'u2': request.user.user_profile}, context_instance=RequestContext(request))   


def home(request):
	return render_to_response('home.html', {}, context_instance=RequestContext(request))


def newproject(request, u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)
	return render_to_response('newproject.html', {'u': u, 'u2': u2}, context_instance=RequestContext(request))


def viewproject(request, project_id):
	p = Project.objects.get(id=project_id)
	profit = p.prof
	exp = p.exp.all()
	revenues = p.revenues.all()
	return render_to_response('viewproject.html', {'p':p, 'profit':profit, 'e':exp, 'revenues':revenues}, context_instance=RequestContext(request))


def updateproject(request, post_id):
	p = Project.objects.get(id=post_id)
	profit = p.prof
	exp = p.exp.all()
	revenues = p.revenues.all()

	if request.POST:
		newname = request.POST['newname']
		p.pname = newname;
		p.save()


		"""getting the new profit date and updating it"""
		profit_date = request.POST['newprofitdate']
		profit.profit_date = profit_date;
		profit.save()


		"""getting the new revenues"""
		total_revenues_amounts1 = 0 
		for r in revenues:
			revenue_name = request.POST['revenue_name[%d]'%r.id]
			revenue_amount = request.POST['revenue_amount[%d]'%r.id]
			revenue_date = request.POST['revenue_date[%d]'%r.id]   
			r.revenue_name = revenue_name
			r.revenue_amount = revenue_amount
			r.revenue_date = revenue_date
			r.save()
			"""getting old amounts sum"""
			total_revenues_amounts1 += int(r.revenue_amount)

		#part of adding expenses men awel wegdeed#
		revenue_names = []
		revenue_amounts = []
		revenue_dates = []    
		done = False
		i=0
		while(not done):
			try:
				revenue_names.append(request.POST['revenue_names[%d]'%i])
				revenue_amounts.append(request.POST['revenue_amounts[%d]'%i])
				revenue_dates.append(request.POST['revenue_dates[%d]'%i])       
				i+=1
			except:
				done=True


		j=0;
		total_revenues_amounts2 = 0  
		while(j<i):
			revenue = Revenue(revenue_name = revenue_names[j], revenue_amount = revenue_amounts[j], revenue_date = revenue_dates[j])
			revenue.save()
			p.revenues.add(revenue)
			"""getting new amounts sum""" 
			total_revenues_amounts2 += int(revenue.revenue_amount)
			j+=1

		p.save()


		"""getting the new expenses"""
		total_expenses_amounts1 = 0
		for e in exp:
			name = request.POST['exp_name[%d]'%e.id]
			amount = request.POST['exp_amount[%d]'%e.id]
			expense_date = request.POST['expense_date[%d]'%e.id]    
			e.ename = name
			e.eamount = amount
			e.expense_date = expense_date
			e.save()
			"""getting old amounts sum"""
			total_expenses_amounts1 += int(e.eamount)


		#part of adding expenses men awel wegdeed#
		enames = []
		eamounts = []
		expense_dates = []        
		done = False
		i=0
		while(not done):
			try:
				enames.append(request.POST['ename[%d]'%i])
				eamounts.append(request.POST['eamount[%d]'%i])
				expense_dates.append(request.POST['expense_date[%d]'%i])    
				i+=1
			except:
				done=True


		j=0;
		total_expenses_amounts2 = 0 
		while(j<i):
			e = Expense(ename = enames[j], eamount = eamounts[j], expense_date = expense_dates[j])
			e.save()
			p.exp.add(e)
			"""getting new amounts sum""" 
			total_expenses_amounts2 += int(e.eamount)
			j+=1

		p.save()


		"""updating the net profit"""
		profit.pamount = total_revenues_amounts1 + total_revenues_amounts2 - total_expenses_amounts1 - total_expenses_amounts2;
		profit.save()


		return render_to_response('viewproject.html', {'p':p, 'profit':profit, 'e':exp, 'revenues':revenues}, context_instance=RequestContext(request))

	else:
		return render_to_response('updateproject.html', {'p':p, 'profit':profit, 'e':exp, 'revenues':revenues}, context_instance=RequestContext(request))


def myprojects(request, u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)

	if request.POST:
		project_name = request.POST['project_name']
		gross_profit_date = request.POST['profit_date']

		temporary_profit = Gprofit(pamount = 0, profit_date = gross_profit_date)
		temporary_profit.save()

		project = Project(pname=project_name, prof=temporary_profit, client=u2)
		project.save()


		"""getting all revenues made in a new project and 
		putting them in the project attribute -revenues-"""

		revenue_names = []
		revenue_amounts = []
		revenue_dates = []
		done1 = False
		a=0
		while(not done1):
			try:
				revenue_names.append(request.POST['revenue_name[%d]'%a])
				revenue_amounts.append(request.POST['revenue_amount[%d]'%a])
				revenue_dates.append(request.POST['revenue_date[%d]'%a])
				a+=1
			except:
				done1=True


		"""creating revenues"""
		x=0;
		total_revenues_amounts = 0
		while(x<a):
			revenue = Revenue(revenue_name = revenue_names[x], revenue_amount = revenue_amounts[x], revenue_date = revenue_dates[x])
			revenue.save()
			total_revenues_amounts += int(revenue.revenue_amount)
			project.revenues.add(revenue)
			project.save()
			x+=1

		
		"""getting all expenses made in a new project and 
		putting them in the project attribute -expenses-"""

		enames = []
		eamounts = []
		expense_dates = []
		done2 = False
		b = 0
		while(not done2):
			try:
				enames.append(request.POST['ename[%d]'%b])
				eamounts.append(request.POST['eamount[%d]'%b])
				expense_dates.append(request.POST['expense_date[%d]'%b])
				b+=1
			except:
				done2=True


		"""creating expenses"""
		y=0;
		total_expenses_amounts = 0
		while(y<b):
			e = Expense(ename = enames[y], eamount = eamounts[y], expense_date = expense_dates[y])
			e.save()
			total_expenses_amounts += int(e.eamount)
			project.exp.add(e)
			project.save()
			y+=1
		

		"""calculating gross profit and use it to create a new project"""

		gross_profit_amount = total_revenues_amounts - total_expenses_amounts
		gross_profit = Gprofit(pamount = gross_profit_amount, profit_date = gross_profit_date)
		gross_profit.save()

		project.prof = gross_profit
		project.save()


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

            #send_mail('subject is put here', 'message is here', 'from_email', 'to_list - which is the list of emails I want to send the mail to, in this case one', 'fail_silently=True')
            subject = 'Welcome to Finance Web App'
            message = 'You are now a registered user on Finance Web App. We are at your service, we hope you find all that you need here.'
            from_email = settings.EMAIL_HOST_USER
            to_list = [user.email, settings.EMAIL_HOST_USER]

            send_mail(subject, message, from_email, to_list, fail_silently=True)

            messages.success(request, 'Thank you for registering, you will receive an email shortly')

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

def viewallposts(request):
	if request.POST:
		title= request.POST['title']
		text= request.POST['text']
		Post(title=title, text=text).save()

	return render_to_response('Allposts.html', {
		 	'posts':Post.objects.all(),
		 	}, context_instance=RequestContext(request))


def viewpost(request, post_id):
	p = Post.objects.get(id=post_id)

	if request.POST:
		comment_text = request.POST['comment']
		c = comment(post=p, comment=comment_text)
		c.save()
	return render_to_response('viewpost.html', {
       	'p':p,
        'comments': comment.objects.filter(post=p),

    }, context_instance=RequestContext(request))


def makepost(request):
	if request.POST:
		title= request.POST['title']
		text= request.POST['text']
		Post(title=title, text=text).save()
	return render_to_response('newpost.html', {
		 	'posts':Post.objects.all(),
		 	}, context_instance=RequestContext(request))

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


def deletepost(request,post_id,u_id):
	u = User.objects.get(id=u_id)
	u2 = UserProfile.objects.get(user=u)
	
	if request.POST:
		post= Post.objects.get(id=post_id)
		post.delete()
		return render_to_response('viewpost.html', {'posts':Post.objects.all(), 'u': u, 'u2': u2}, context_instance=RequestContext(request))


def viewexpenses(request, project_id):
	project = Project.objects.get(id=project_id)
	expenses = project.exp.all()
	return render_to_response('viewexpenses.html', {'project':project, 'expenses':expenses}, context_instance=RequestContext(request))


def viewgrossprofit(request, project_id):
	project = Project.objects.get(id=project_id)
	grossprofit = project.prof
	return render_to_response('viewgrossprofit.html', {'project':project, 'grossprofit':grossprofit}, context_instance=RequestContext(request))


def overview_project(request, project_id):
	project = Project.objects.get(id=project_id)
	grossprofit = project.prof
	expenses = project.exp.all()
	revenues = project.revenues.all()

	cm = datetime.now().month
	current_month = calendar.month_name[cm]
	current_year = datetime.now().year


	totalrevenues = 0
	for r in revenues:
		if r.revenue_date.year == current_year:
			if r.revenue_date.month == cm: 
				totalrevenues += r.revenue_amount


	totalexpenses = 0
	for x in expenses:
		if x.expense_date.year == current_year:
			if x.expense_date.month == cm: 
				totalexpenses += x.eamount


	net_profit = totalrevenues - totalexpenses

	return render_to_response('overview_project.html', {'project':project, 'grossprofit':grossprofit, 'expenses':expenses, 'revenues':revenues, 'cm':cm, 'current_month':current_month, 'current_year':current_year, 'net_profit':net_profit}, context_instance=RequestContext(request))


def viewrevenues(request, project_id):
	project = Project.objects.get(id=project_id)
	revenues = project.revenues.all()
	return render_to_response('viewrevenues.html', {'project':project, 'revenues':revenues}, context_instance=RequestContext(request))












