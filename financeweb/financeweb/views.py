from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from app1.models import user
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

	return render_to_response('signup.html', {}, context_instance=RequestContext(request))
