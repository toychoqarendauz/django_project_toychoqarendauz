from django.shortcuts import render


def HomePage(request):
	return render(request, 'pages/home-page.html')