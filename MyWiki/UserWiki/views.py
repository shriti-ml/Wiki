from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from .models import WikiInformation
from .forms import WikiForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
    
def homepage(request):
	topics = WikiInformation.objects.all() #queryset containing all books we just created
	return render(request=request, template_name="home.html", context={'topics':topics})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("homepage")


# Create your views here.
def wikiinfo(request):
    if request.method == 'POST':
        form = WikiForm(request.POST)
        if form.is_valid():
            subject = "Wiki Information"
            body = {
                'topic': form.cleaned_data['topic'], 
                'article': form.cleaned_data['article'] 
                }
            article = "\n".join(body.values())
            return redirect ("homepage")
    form = WikiForm()
    return render(request, "wikiinfo.html", {'form':form})

