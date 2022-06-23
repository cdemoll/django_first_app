from django.shortcuts import render
from datetime import datetime

def index(requests):
    date = datetime.today()

    return render(requests, 'index.html', context={'prenom':"Clement", 'date': date} )