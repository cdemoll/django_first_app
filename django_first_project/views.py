from django.shortcuts import render
from datetime import datetime

def index(requests):
    date = datetime.today()

    return render(requests, 'django_first_project/index.html', context={'prenom':"Clement", 'date': date} )