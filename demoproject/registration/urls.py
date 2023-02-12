from . import views
from django.urls import path

urlpatterns = [
    path('b', views.show, name='show'),
    path('log', views.log, name='log'),
    path('logout',views.logout,name='logout')
]
