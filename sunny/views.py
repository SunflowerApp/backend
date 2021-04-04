from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# docker run --name sunflower-db-ps -e POSTGRES_PASSWORD=sunflower_pass -d sunflower_db

def index(request):
    return HttpResponse("Hello, world. You're at the SunflowerApp index.")
