from django.shortcuts import render, redirect
from .models import Kasvattaja, Lemmikki

def landingview(request):
    return render(request, 'landingpage.html')

# Product view´s

def lemmikkilistaview(request):
    lemmikkilista = Lemmikki.objects.all()
    kasvattajalista = Kasvattaja.objects.all()
    context = {'lemmikit': lemmikkilista, 'kasvattajat': kasvattajalista}
    return render (request,"lemmikkilista.html",context)


def addlemmikki(request):
    a = request.POST['lemmikkirotu']
    c = request.POST['unitprice']
    d = request.POST['unitsinstock']
    e = request.POST['kasvattaja']
    
    Lemmikki(lemmikkirotu = a, unitprice = c, unitsinstock = d, kasvattaja = Kasvattaja.objects.get(id = e)).save()
    return redirect(request.META['HTTP_REFERER'])


def confirmdeletelemmikki(request, id):
    lemmikki = Lemmikki.objects.get(id = id)
    context = {'lemmikki': lemmikki}
    return render (request,"confirmdellem.html",context)


def deletelemmikki(request, id):
    Lemmikki.objects.get(id = id).delete()
    return redirect(lemmikkilistaview)


def edit_lemmikki_get(request, id):
        lemmikki = Lemmikki.objects.get(id = id)
        context = {'lemmikki': lemmikki}
        return render (request,"edit_lemmikki.html",context)


def edit_lemmikki_post(request, id):
        item = Lemmikki.objects.get(id = id)
        item.unitprice = request.POST['unitprice']
        item.unitsinstock = request.POST['unitsinstock']
        item.save()
        return redirect(lemmikkilistaview)

def lemmikit_filtered(request, id):
    lemmikkilista = Lemmikki.objects.all()
    filteredlemmikit = lemmikkilista.filter(supplier = id)
    context = {'lemmikit': filteredlemmikit}
    return render (request,"lemmikkilista.html",context)


def kasvattajalistaview(request):
    kasvattajalista = Kasvattaja.objects.all()
    context = {'kasvattajat': kasvattajalista}
    return render (request,"kasvattajalista.html",context)

def addkasvattaja(request):
    a = request.POST['companyname']
    b = request.POST['contactname']
    c = request.POST['address']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['country']
    Kasvattaja(companyname = a, contactname = b, address = c, phone = d, email = e, country = f).save()
    return redirect(request.META['HTTP_REFERER'])
    

def confirmdeletekasvattaja(request, id):
    kasvattaja = Kasvattaja.objects.get(id = id)
    context = {'kasvattaja': kasvattaja}
    return render (request,"confirmdelkas.html",context)


def deletekasvattaja(request, id):
    Kasvattaja.objects.get(id = id).delete()
    return redirect(kasvattajalistaview)


def searchkasvattaja(request):
    search = request.POST['search']
    filtered = Kasvattaja.objects.filter(companyname__icontains=search)
    context = {'kasvattajat': filtered}
    return render (request,"kasvattajalista.html",context)
