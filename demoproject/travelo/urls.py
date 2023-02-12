from . import views
from django.urls import path

urlpatterns = [

    path('',views.trvl,name='trvl'),


]
