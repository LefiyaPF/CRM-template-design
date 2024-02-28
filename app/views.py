from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request,"homepage.html")

def hidden_cards(request):
    return render(request,"hidden_cards.html")