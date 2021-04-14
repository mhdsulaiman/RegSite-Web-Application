from django.shortcuts import render

def HomeView(request, *args, **kwargs):
    return render(request, "Regsite/Home.html", {})