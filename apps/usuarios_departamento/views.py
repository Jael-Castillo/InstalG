from django.shortcuts import render

# Create your views here.

def usd(request):
	return render(request, 'usuarios_departamento/add_usd.html', {})