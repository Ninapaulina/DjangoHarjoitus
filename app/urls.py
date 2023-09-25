
from django.urls import path

from .views import  kasvattajalistaview, lemmikkilistaview, addkasvattaja, addlemmikki, \
   deletelemmikki, deletekasvattaja, confirmdeletelemmikki, confirmdeletekasvattaja, lemmikit_filtered, \
   loginview, login_action, logout_action

urlpatterns = [
   #path('', landingview),

   # Login & logout
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),


   path('kasvattajat/', kasvattajalistaview),
   path('lemmikit/', lemmikkilistaview),
   path('add-lemmikki/', addlemmikki),
   path('add-kasvattaja/', addkasvattaja),
   path('delete-lemmikki/<int:id>/', deletelemmikki),
   path('confirm-delete-lemmikki/<int:id>/', confirmdeletelemmikki),
   path('delete-kasvattaja/<int:id>/', deletekasvattaja),
   path('confirm-delete-kasvattaja/<int:id>/', confirmdeletekasvattaja),
   path('lemmikit-by-kasvattaja/<int:id>/', lemmikit_filtered)
  
]
