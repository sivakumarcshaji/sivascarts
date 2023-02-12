from . import views
from django.urls import path

urlpatterns = [

    path('plus/', views.plus, name="plus"),
    path('multy/', views.multy, name="multy"),
    path('division/', views.division, name="division"),
    path('minus/', views.minus, name="minus")
]
