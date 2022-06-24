from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'blog/index.html')

def article01(requests):
    return render(requests, 'blog/article01.html')

def article02(requests):
    return render(requests, 'blog/article02.html')

def article03(requests):
    return render(requests, 'blog/article03.html')