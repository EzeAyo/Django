from django.shortcuts import render
def home(request):
    return render(request, 'itreporting/home.html', {'titile': 'Welcome Page'})
def about(request):
    return render(request, 'itreporting/about.html', {'titile': 'About us'})
def contact(request):
   return render(request, 'itreporting/contact.html')
def profile(request):
    return render(request, 'users/profile.html')
# Create your views here.
