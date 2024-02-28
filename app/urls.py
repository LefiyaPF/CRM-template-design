from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("hidden_cards",views.hidden_cards,name="hidden_cards"),
]