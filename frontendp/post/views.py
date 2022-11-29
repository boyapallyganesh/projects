from django.shortcuts import render

# Create your views here.
def main(request):
    return render(request, 'post/main.html')
def editpost(request):
    return render(request, 'post/editpost.html')
def createpost(request):
    return render(request, 'post/createpost.html')
def detail(request):
    return render(request, 'post/detail.html')