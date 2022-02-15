from unicodedata import category
from django.shortcuts import render
from .models import Skills, Category, Home, Profile, About, Portfolio
from datetime import datetime
import time

# Create your views here.
def home(request):
    return render(request,"jobs/home.html")

def student(request):
    return render(request,"jobs/student.html")

def index(request):
    home=Home.objects.latest("updateed")
    about = About.objects.latest("updated")
    profiles = Profile.objects.filter(about=about)
    categories = Category.objects.all()
    portfolios = Portfolio.objects.all()
    
    
    ## get the current time
    # now = datetime.now().time()
    t = time.localtime()
    now = time.strftime("%H:%M:%S", t)
    
    context={
        "home":home,
        "about":about,
        "profiles":profiles,
        "categories":categories,
        "portfolios":portfolios,
        "now":now
    }
    return render(request,"jobs/index.html",context)

