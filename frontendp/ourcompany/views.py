from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request, 'company/about.html')
def contactus(request):
    return render(request, 'company/contact.html')