from django.shortcuts import render
from django.template import loader
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from .models import Profile

# Create your views here.

def home(request):

    return render(request, 'website/templates/index.html')

@login_required
def store_data(request):
	if request.method != 'POST':
		return render(request, 'website/templates/data-entry.html')

@csrf_exempt
def encryption_key_verify(request):
	user = request.user
	profile = Profile.objects.get(user=user)
	print request.POST.get('encryption_key')
	print profile.encr_key
	if(request.POST.get('encryption_key') == profile.encr_key):
		print "yes"
		return HttpResponse('Yes')
	else:
		print "No"
		return HttpResponse('No')



@csrf_exempt
def generate_id(request):
	print request.POST.get('name')
	
	return HttpResponse("abcd,efgh,cvfg")

@csrf_exempt
def validate_data(request):
	result = request.POST.get('result')
	validated = "Yes"
	return HttpResponse(validated)

@csrf_exempt
@login_required
def profile_data(request):
	if request.method == 'POST':
		user = request.user
		name = request.POST.get('name')
		print name
		address = request.POST.get('address')
		print address
		dob = request.POST.get('dob')
		print dob
		encrky = request.POST.get('encrky')
		print encrky
		profile = Profile(user=user, name=name, address=address, dob=dob, encr_key=encrky)
		profile.save()

		return HttpResponse("Done")

	else:
		user = request.user
		print Profile.objects.filter(user=user).count()
		if(Profile.objects.filter(user=user).count()==0):
			return render(request, 'website/templates/profile.html')
		else:
			profile = Profile.objects.get(user=user)
			print profile
			print profile.name
			context = {
	        'name': profile.name,
	        'address': profile.address,
	        'dob': profile.dob,
	        }
    		context.update(csrf(request))
    		return render(request, 'website/templates/profile-page.html', context)

@csrf_exempt
@login_required
def edit_profile(request):
	if request.method == 'POST':
		user = request.user
		name = request.POST.get('name')
		print name
		address = request.POST.get('address')
		print address
		dob = request.POST.get('dob')
		print dob
		encrky = request.POST.get('encrky')
		print encrky
		profile = Profile.objects.get(user=user)
		profile.name = name
		profile.address = address
		profile.dob = dob
		profile.save()

		return HttpResponse("Done")

	else:
		user = request.user
		print Profile.objects.filter(user=user).count()
		if(Profile.objects.filter(user=user).count()==0):
			return HttpResponseRedirect("/")
		else:
			profile = Profile.objects.get(user=user)
			print profile
			print profile.name
			context = {
	        'name': profile.name,
	        'address': profile.address,
	        'dob': profile.dob,
	        }
    		context.update(csrf(request))
    		return render(request, 'website/templates/edit-profile-page.html', context)

