from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Привет, братки!')

def group_posts(request, slug):
    return HttpResponse(f'Вы на странице какого-то {slug}')