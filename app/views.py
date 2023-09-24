from django.shortcuts import render

def landingview(request):
    return render(request, 'landingpage.html')

def lemmikkilistaview(request):
    return render(request, 'lemmikkilista.html')

def kasvattajalistaview(request):
    return render(request, 'kasvattajalista.html')



