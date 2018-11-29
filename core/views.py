from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

#def home(request):
#   return render( request, "core/home.html")

def bolsa(request):
    return render( request, "core/bolsa-de-trabajo.html")

def directorio(request):
    return render( request, "core/directorio.html")

def registro(request):
	if request.method =='POST':	
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = UserCreationForm()

		args = {'form': form}
		return render(request, 'core/registro.html', args)