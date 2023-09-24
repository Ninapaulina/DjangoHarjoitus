
from django.urls import path

from .views import landingview, kasvattajalistaview, lemmikkilistaview, addkasvattaja, addlemmikki

urlpatterns = [
   path('', landingview),

   path('kasvattajat/', kasvattajalistaview),
   path('lemmikit/', lemmikkilistaview),
   path('add-lemmikki/', addlemmikki),
   path('add-kasvattaja/', addkasvattaja),
   


]
