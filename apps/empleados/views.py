from django.shortcuts import render


def index(request):
	return render(request, 'empleados/list.html', {})

def detail(request, pk):
	return render(request, 'empleados/detail.html', {'pk': pk})

def form(request):
	return render(request, 'empleados/form.html', {})
