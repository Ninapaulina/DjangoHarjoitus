
from django.urls import path

from .views import landingview, kasvattajalistaview, lemmikkilistaview

urlpatterns = [
   path('', landingview),

   path('kasvattajat/', kasvattajalistaview),

   path('lemmikit/', lemmikkilistaview),
   


]
