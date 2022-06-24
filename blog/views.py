from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'blog/index.html')

def article(requests, numero_article):
    if numero_article in ['01','02', '03']:
        return render(requests, f"blog/article{numero_article}.html")
    return render(requests, f"blog/article_not_found.html")
